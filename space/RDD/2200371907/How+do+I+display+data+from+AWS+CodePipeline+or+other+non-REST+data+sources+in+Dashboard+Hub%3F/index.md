# How do I display data from AWS CodePipeline or other non-REST data sources in Dashboard Hub?

Custom Reports only supports REST API sources. However, you can consider alternative solutions. To extract data from AWS CodePipeline you could try one of the following:

1. **Custom REST Endpoint**  
   Writing your own REST backend is currently the most flexible way to connect **CDK commands** with Dashboard Hub. By exposing the required pipeline data via a REST API, you can use our **Custom Report gadgets** to visualize it seamlessly.

1. **Using AWS Lambda & API Gateway**

- You could deploy a simple **AWS Lambda function** that executes the required **CDK commands** and processes the pipeline summary.
- Use **API Gateway** to expose this Lambda function as a REST endpoint, which can then be consumed by Dashboard Hub’s Custom Report gadget.
- This approach avoids setting up a full REST backend and leverages AWS-native services.