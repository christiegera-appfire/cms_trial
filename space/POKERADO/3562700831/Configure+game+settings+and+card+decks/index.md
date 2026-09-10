# Configure game settings and card decks

**Estimated time**: About 5 minutes

Configure the default estimation fields and card decks used for new Planning Poker games. These settings apply to every new game you create, but you can override them during [game creation](/cms_trial/space/POKERADO/3315008376/Create+game/).

To open the settings page, go to **Boards** > **Planning Poker** > **Settings**.

## What you’ll configure

On this page you can:

- Choose where estimates are saved for each work item type.
- Select the default card deck used during estimation.
- Create custom card decks.
- Control where Planning Poker appears in Azure DevOps.

## Planning Poker settings

![Planning Poker Settings page showing default estimation fields, card deck mappings, and extension visibility settings.](/cms_trial/assets/f4a4858d-ae71-45d0-a389-7832919ee29d.png)

## Estimation field and card deck mapping

![Work item type mapping showing estimation fields and assigned card decks.](/cms_trial/assets/33c3df18-a557-4d06-b2ed-8139623219e4.png)

For each Azure DevOps work item type in your organization (the exact list depends on your process template, for example User Story, Bug, and Task), you can set:

- **Estimation field**: the Azure DevOps field a game's final estimate writes back to. This is a searchable dropdown listing every field on that work item type, including non-numeric fields like Title, State, or Priority, so pick a numeric field like Effort, Remaining Work, or Story Points. Choosing **-- None --** means estimates for that work item type won't be saved anywhere, the game still runs, but nothing gets written back.
- **Estimation values**: the voting deck estimators use for that work item type. See Card decks below for the available options.

Most work item types default to **-- None --**. If a game's estimates aren't saving, check this setting first.

## Card decks

Each work item type's Estimation values row has a deck-type dropdown and an editable value list. Available deck types:

| **Deck type** | **Best for** | **Values** |
| --- | --- | --- |
| **Fibonacci** | Most Scrum teams estimating relative effort | `0, 1, 2, 3, 5, 8, 13` |
| **Modified Fibonacci** | Teams using a wider estimation scale or fractional values | `0, 0.5, 1, 2, 3, 5, 8, 13, 20, 40, 100` |
| **T-Shirt** | High-level estimation and early planning | `XXS=0.5, XS=1, S=2, M=3, L=5, XL=8, XXL=13` |
| **S/M/L** | Simple relative sizing | `S=1, M=3, L=5` |
| **Custom** | Teams using their own estimation scale | Fully customizable to whatever values your team needs. |

## Create a custom card deck

To create your own estimation deck:

1. Select **Custom** for the work item type.
2. Edit the adjacent value list.
3. Save your changes.

The custom values become the default deck for new Planning Poker games that use that work item type.

## Extension visibility

Planning Poker appears in the *Work Item details view* and the *Board view* based on the scopes granted when the app was installed. See [Requested permissions](/cms_trial/space/POKERADO/660308966/Requested+permissions/).