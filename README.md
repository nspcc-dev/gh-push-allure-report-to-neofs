<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./.github/logo_dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./.github/logo_light.svg">
    <img src="./.github/logo_light.svg"  width="500px" alt="NeoFS logo">
  </picture>
</p>
<p align="center">
  <a href="https://fs.neo.org">NeoFS</a> is a decentralized distributed object storage integrated with the <a href="https://neo.org">NEO Blockchain</a>.
</p>

# GitHub Action to Publish Allure report from nspcc-dev projects to NeoFS
This action allows you to publish [Allure reports](https://github.com/allure-framework/allure2)
to [NeoFS](https://fs.neo.org/).

Of course, you can use this action unchanged in your forks, or if you have a similar report structure.
This action is also a great example of how to use [publish-to-neofs](https://github.com/marketplace/actions/publish-to-neofs).
We recommend using [publish-to-neofs](https://github.com/marketplace/actions/publish-to-neofs) because 
[publish-to-neofs](https://github.com/marketplace/actions/publish-to-neofs) is a more flexible tool.


[Here](https://neospcc.medium.com/neofs-t5-testnet-has-been-started-ae75c30e856b) is a good article on how to get
started using the NeoFS testnet, this may be useful if you have no experience with NeoFS and want to get started with
the test network.

## Supported platforms
This action supports the following platforms:
- Linux x64

This action tested on the following runners:
- [Ubuntu 22.04 GitHub-hosted runners](https://github.com/actions/runner-images/blob/main/images/linux/Ubuntu2204-Readme.md)

# Configuration

## GitHub secrets
The following Sensitive information must be passed as
[GitHub Actions secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).
It is very important to use SECRETS and NOT variables, otherwise your wallet, password and token will be available to
the whole internet.

| Key                     | Value                                                                                                                                                                      | Required | Default |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------|
| `NEOFS_WALLET`          | Base64-encoded NEP-6 Neo N3 wallet. To create N3 wallet: `neo-go wallet init -w wallet.json -a` The output of this command should be here: 'cat wallet.json &#124; base64' | **Yes**  | N/A     |
| `NEOFS_WALLET_PASSWORD` | N3 wallet password                                                                                                                                                         | **Yes**  | N/A     |

Please keep sensitive data safe.

## GitHub environment variables

### NeoFS network environment variables
The following variables must be passed as
[GitHub Actions vars context](https://docs.github.com/en/actions/learn-github-actions/variables#using-the-vars-context-to-access-configuration-variable-values) 
or [GitHub Actions environment variables](https://docs.github.com/en/actions/learn-github-actions/variables).

Up-to-date information about NeoFS network can be seen on https://status.fs.neo.org.

If you are using the NeoFS mainnet, we recommend that you do not change `NEOFS_NETWORK_DOMAIN`
and `NEOFS_HTTP_GATE` environment variables.

| Key                    | Value                                                                                 | Required | Default                |
|------------------------|---------------------------------------------------------------------------------------|----------|------------------------|
| `NEOFS_NETWORK_DOMAIN` | Rpc endpoint domain address                                                           | **No**   | st1.storage.fs.neo.org |
| `NEOFS_HTTP_GATE`      | HTTP Gateway domain address                                                           | **No**   | http.fs.neo.org        |
| `STORE_OBJECTS_CID`    | Container ID for your data. For example: 7gHG4HB3BrpFcH9BN3KMZg6hEETx4mFP71nEoNXHFqrv | **Yes**  | N/A                    |


### Workflow environment variables
The following variables must be passed as
[GitHub Actions vars context](https://docs.github.com/en/actions/learn-github-actions/variables#using-the-vars-context-to-access-configuration-variable-values)
or [GitHub Actions environment variables](https://docs.github.com/en/actions/learn-github-actions/variables).

| Key                    | Value                                                                                                                                                                                                                                     | Required | Default                                    |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------|
| `ALLURE_RESULTS_DIR`   | Path to the directory where the Allure test report is stored                                                                                                                                                                              | **Yes**  | N/A                                        |
| `ALLURE_GENERATED_DIR` | Path to the directory that will be used to store the generated report. This directory will be created automatically if it does not exist. ATTENTION - all files that were in this directory before the action was started will be deleted | **No**   | ./tests/neofs-test-allure-generated-report |

### Expiration period environment variables
The following variables must be passed as 
[GitHub Actions vars context](https://docs.github.com/en/actions/learn-github-actions/variables#using-the-vars-context-to-access-configuration-variable-values)
or [GitHub Actions environment variables](https://docs.github.com/en/actions/learn-github-actions/variables).

These environment variables are responsible for the storage time of the results in the storage network in epochs 
(in the mainnet, an epoch is approximately equal to one hour, so we can assume that values are specified in HOURS).

After the period is over, the data will be deleted. They are convenient to use for log rotation or test reports.

They default to 0, in which case the data will be stored until they are manually deleted.
We recommend setting a reasonable and convenient for work expiration period, for example, a month (744 hours).

For results from releases, there is no expiration date, they will be stored until they are manually deleted.


| Key                   | Value                                                                                                                                                                                          | Required | Default |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------|
| `PR_LIFETIME`         | Number of epochs for artifacts created as a result of [opening or modifying a PR](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request) to stay valid | **No**   | 0       |
| `MASTER_LIFETIME`     | Number of epochs for artifacts created as a result of [master/main branch modification](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#push) to stay valid   | **No**   | 0       |
| `MANUAL_RUN_LIFETIME` | Number of epochs for artifacts created as a result of [manually run](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_dispatch)                       | **No**   | 0       |
| `OTHER_LIFETIME`      | Number of epochs for artifacts created as a result of other events                                                                                                                             | **No**   | 0       |

## Output

| Key                   | Output example                                                                               |
|-----------------------|----------------------------------------------------------------------------------------------|
| `REPORT_NEOFS_URL`    | https://http.storage.fs.neo.org/HXSaMJXk2g8C14ht8HSi7BBaiYZ1HeWh2xnWPGQCg4H6/872-1696332227/ |
| `COMBINED_REPORT_DIR` | https://http.storage.fs.neo.org/HXSaMJXk2g8C14ht8HSi7BBaiYZ1HeWh2xnWPGQCg4H6/872-1696332227  |

# Dependencies

## Python
This action has no dependencies that need to be installed separately.
But Python 3, neofs-cli and allure-combine are installed inside actions.

# Examples

```yml
name: Publish Allure result to NeoFS
on:
  push:
    branches: [ master ]
env:
  ALLURE_RESULTS_DIR: ${GITHUB_WORKSPACE}/allure-results
jobs:
  push-to-neofs:
    runs-on: ubuntu-latest
    steps:
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11.6'
          
      - name: Checkout neofs-testcases repository
        uses: nspcc-dev/checkout@v4
        with:
          repository: nspcc-dev/neofs-testcases
          ref: 'master'
          path: neofs-testcases
          
#          ...
#          Prepare test environment
#          ...
          
      - name: Run tests and store allure result
        run: |
          source venv/bin/activate && pytest --alluredir=${{ env.ALLURE_RESULTS_DIR }} pytest_tests/testsuites
        working-directory: neofs-testcases
  
      - uses: actions/checkout@v4
      - name: Publish to NeoFS
        uses: nspcc-dev/gh-push-allure-report-to-neofsfs@master
        with:
          NEOFS_WALLET: ${{ secrets.NEOFS_WALLET }}
          NEOFS_WALLET_PASSWORD: ${{ secrets.NEOFS_WALLET_PASSWORD }}
          NEOFS_NETWORK_DOMAIN: ${{ vars.NEOFS_NETWORK_DOMAIN }}
          NEOFS_HTTP_GATE: ${{ vars.NEOFS_HTTP_GATE }}
          STORE_OBJECTS_CID: ${{ vars.STORE_OBJECTS_CID }}
          PR_EXPIRATION_PERIOD: ${{ vars.PR_EXPIRATION_PERIOD }}
          MASTER_EXPIRATION_PERIOD: ${{ vars.MASTER_EXPIRATION_PERIOD }}
          MANUAL_RUN_EXPIRATION_PERIOD: ${{ vars.MANUAL_RUN_EXPIRATION_PERIOD }}
          OTHER_EXPIRATION_PERIOD: ${{ vars.OTHER_EXPIRATION_PERIOD }}
          ALLURE_RESULTS_DIR: ${{ env.ALLURE_RESULTS_DIR }}
```

