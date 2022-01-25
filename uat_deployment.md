Deploying to UAT
================

**TL;DR**: Add the `deploy uat` label to a PR to initiate a UAT deployment. **You must thoroughly check the PR before adding this label**. Leave the label on the PR when it is merged/closed for automatic teardown and image cleanup.

UAT Environment
---------------

There is an isolated, standalone k3s instance (Flex 15254) used for deploying containers from pull requests made against this repository. These instances then become available for viewing at https://pr-$PRNUMBER.docsuat.devops.ukfast.co.uk.

To deploy a PR to the UAT environment, you **must** check the PR to ensure there are no malicious changes. If you are happy, add the `deploy uat` label, which will initiate a workflow to build containers from the PR and deploy them to the UAT environment. Once the workflow completes, you may need to wait a few moments until the site actually becomes available - you will initially see a 404, then a 'Service Unavailable' message if you're too quick to view the deployment.

If further changes are pushed to the PR and you wish to view them in UAT, you must remove and re-add the `deploy uat` label to initiate an updated deployment. This is so you can again check for malicious commits before pushing something into the UAT environment.

You must leave the `deploy uat` label on the PR when the PR is closed or merged. This will trigger a workflow to teardown the UAT environment and delete the container images from ghcr.io.

Only UKFast organisation users with push access to the repository will be able to add and remove labels.
