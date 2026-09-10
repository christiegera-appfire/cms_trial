# Adjust an estimate according to assignee

## Problem

You want to simplify estimation of difficult tasks when using Agile frameworks. For example, you are unsure which team member will pick up a task, and you can only assign it a rough estimate. In the event of new team member, estimation might be made even more difficult given the learning and adaptation curve. Thus, completion time may vary from one team member to another.

## Solution

To solve this problem, one option is to customize the estimate.

For example, consider a task estimated at 1 day. While one team member may need 1 day 4 hours to resolve it, another might be able to resolve it in 6 hours.

By keeping track of the error margin for each user, and the average of issues worked on, you can ensure a better starting estimate for upcoming tasks. If a user is consistently taking longer than the average by, for example, 20%, then you can anticipate and raise the estimate by 20% for them.

To do this, add two actions:

1. **Start Progress**  
   When a user starts progress on an issue, the remaining estimate is recalculated to correspond to their velocity. A user's velocity is the factor by which the original estimate is multiplied to ensure a more accurate approximation.
2. **Resolve Issue**  
   When an issue is resolved, add the difference between the time spent working on the issue and the calculated amount at progress start. Then include this result in future approximations.

Keep track of the parameters by storing them as user properties. The properties take the following two values:

1. User velocity
2. Iterations number (Each time you alter the velocity, you increment this value).

Each user starts with a velocity of 1 and 0 iterations.

## Step 1 - Progress start and estimate recalculation

When a user starts progress on an issue, multiply the original estimate by user velocity. Include the result in the remaining estimate.

This step is recommended only if no time was logged on the issue, as some users work on an issue intermittently.

It is also recommended (with minor adjustments) when the issue is re-assigned. To allow some flexibility, write all the necessary functions in a separate file that you can retrieve from other SIL™ scripts.

#### **Start progress action**

```text
include "common_velocity.incl"; // our "auto-estimate library"
updateRemaining(key); 
```

## Step 2 - Resolving an issue and velocity recalculation

When an issue is resolved, calculate the approximation error and include it in the velocity. You can use it for future estimates.

#### **Resolve issue action**

```text
include "common_velocity.incl"; // our "auto-estimate library"
adjustVelocity(key); 
```

## Step 3 - Add the Environment configuration

Use the SIL™ Environment to store the default velocity (1) as well as the user properties containing the velocity and iterations number.

#### **sil.properties**

```text
default.velocity = 1
user.velocity = jjup.autoestimate.user.velocity
velocity.samples = jjup.autoestimate.velocity.samples
```

SIL Environment variables have been replaced with the more versatile [persistent variables](/cms_trial/space/PSJC/496205909/Persistent+variables/) feature. Unlike environment variables, these variables can be set in the code. Also, they can be specific to each issue, based on issue context.

## Step 4 - Add the library

To include the logic in one file and use it again when re-estimating (for example, in listeners or services), save the following file to your **silprograms** folder.

#### **common\_velocity.incl**

```text
function getUserVelocity(string user){
	if(! userExists(user)){
		number DEFAULT_VELOCITY = silEnv("default.velocity");
		logPrint("DEBUG", "User " + user + " does not exist. Cannot calculate velocity. Using default " + DEFAULT_VELOCITY);
		return DEFAULT_VELOCITY;
	}
	number velocity = getUserProperty(user, silEnv("user.velocity"));

	if(isNull(velocity)){
		string DEFAULT_VELOCITY = silEnv("default.velocity");
		setUserProperty(user, silEnv("user.velocity"), DEFAULT_VELOCITY);
		velocity = DEFAULT_VELOCITY;
	}
	return velocity;
}


function getNoVelocitySamples(string user){
	if(! userExists(user)){
		logPrint("DEBUG", "User " + user + " does not exist. Cannot get number of velocity samples");
		return 0;
	}
	number samples = getUserProperty(user, silEnv("velocity.samples"));

	if(isNull(samples)){
		setUserProperty(user, silEnv("velocity.samples"), 0);
		samples = 0;
	}
	return samples;
}


function setNoSamples(string user, number noSamples){
	if(! userExists(user)){
		logPrint("DEBUG", "User " + user + " does not exist. Cannot set velocity samples.");
		return ;
	}
	setUserProperty(user, silEnv("velocity.samples"), noSamples);
}


function setUserVelocity(string user, number velocity){
	if(! userExists(user)){
		logPrint("DEBUG", "User " + user + " does not exist. Cannot set velocity.");
		return ;
	}
	setUserProperty(user, silEnv("user.velocity"), velocity);
}


function getWorkForUser(string user, string issKey){
	number [] ids = getWorklogIdsForUser(user, issKey);
	interval intvl = "0h";
	if(isNull(ids) || size(ids) == 0){
		return intvl;
	}
	for(number wlid in ids){
		intvl += getWorklogLoggedHours(wlid);
	}
	return intvl;
}


function isSoloWork(string user, string issKey){
	return %issKey%.spent == getWorkForUser(user, issKey);
}


function adjustVelocity(string issKey){
	string user = %issKey%.assignee;
	if(!isSoloWork(user, issKey)){
		logPrint("DEBUG", "User" + user + " did not work all by himself on issue " + issKey + ". Cannot update velocity");
		return;
	}
	number noSamples = getNoVelocitySamples(user);
	number velocity = getUserVelocity(user);
	number estimateWithVelocity = %issKey%.originalEstimate["TOMILLIS"] * velocity;
	number currentRatio = %issKey%.spent["TOMILLIS"] /estimateWithVelocity;
	number newVelo = (velocity * noSamples + currentRatio) / (noSamples + 1);
 
	setUserVelocity(user, newVelo);
	setNoSamples(user, noSamples + 1);
	logPrint("INFO", "Updated user " + user + " velocity from " + velocity + " to " + newVelo + " based on " + (noSamples+1) + " samples");
}


function updateRemaining(string issKey){
	if(%issKey%.spent > "0d" ){
		logPrint("DEBUG", "Work already logged. Not altering remaining estimate.");
		return;
	}
	number velocity = getUserVelocity(%issKey%.assignee);
	number remainingMillis = %issKey%.originalEstimate["TOMILLIS"];
	%issKey%.remaining = remainingMillis * velocity;
} 
```

You can modify the functions in this example to account for other users that have worked on the same issue.