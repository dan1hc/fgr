"""
Regex patterns to redact common, sensitive data.

Sourced from trivy / aqua.
https://github.com/aquasecurity/trivy/blob/main/pkg/fanal/secret/builtin-rules.go

"""

import re

from . import dtypes


REDACTION_PATTERNS = [
	dtypes.RePatternDict(
		ID='aws-access-key-id',
		Severity='CRITICAL',
		Title='AWS Access Key ID',
		Regex=re.compile(r"""(?P<secret>(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16})"""),
		),
	dtypes.RePatternDict(
		ID='aws-secret-access-key',
		Severity='CRITICAL',
		Title='AWS Secret Access Key',
		Regex=re.compile(r"""(?i)(^|\s+)(?P<secret>[A-Za-z0-9\/\+=]{40})"""),
		),
	dtypes.RePatternDict(
		ID='github-pat',
		Title='GitHub Personal Access Token',
		Severity='CRITICAL',
		Regex=re.compile(r"""ghp_[0-9a-zA-Z]{36}"""),
		),
	dtypes.RePatternDict(
		ID='github-oauth',
		Title='GitHub OAuth Access Token',
		Severity='CRITICAL',
		Regex=re.compile(r"""gho_[0-9a-zA-Z]{36}"""),
		),
	dtypes.RePatternDict(
		ID='github-app-token',
		Title='GitHub App Token',
		Severity='CRITICAL',
		Regex=re.compile(r"""(ghu|ghs)_[0-9a-zA-Z]{36}"""),
		),
	dtypes.RePatternDict(
		ID='github-refresh-token',
		Title='GitHub Refresh Token',
		Severity='CRITICAL',
		Regex=re.compile(r"""ghr_[0-9a-zA-Z]{76}"""),
		),
	dtypes.RePatternDict(
		ID='github-fine-grained-pat',
		Title='GitHub Fine-grained personal access tokens',
		Severity='CRITICAL',
		Regex=re.compile(r"""github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59}"""),
		),
	dtypes.RePatternDict(
		ID='gitlab-pat',
		Title='GitLab Personal Access Token',
		Severity='CRITICAL',
		Regex=re.compile(r"""glpat-[0-9a-zA-Z\-\_]{20}"""),
		),
	dtypes.RePatternDict(
		ID='private-key',
		Title='Asymmetric Private Key',
		Severity='HIGH',
		Regex=re.compile(r"""(?i)-----\s*?BEGIN[ A-Z0-9_-]*?PRIVATE KEY( BLOCK)?\s*?-----[\s]*?(?P<secret>[\sA-Za-z0-9=+/\\\r\n]+)[\s]*?-----\s*?END[ A-Z0-9_-]*? PRIVATE KEY( BLOCK)?\s*?-----"""),
		),
	dtypes.RePatternDict(
		ID='shopify-token',
		Title='Shopify token',
		Severity='HIGH',
		Regex=re.compile(r"""shp(ss|at|ca|pa)_[a-fA-F0-9]{32}"""),
		),
	dtypes.RePatternDict(
		ID='slack-access-token',
		Title='Slack token',
		Severity='HIGH',
		Regex=re.compile(r"""xox[baprs]-([0-9a-zA-Z]{10,48})"""),
		),
	dtypes.RePatternDict(
		ID='stripe-publishable-token',
		Title='Stripe Publishable Key',
		Severity='LOW',
		Regex=re.compile(r"""(?i)pk_(test|live)_[0-9a-z]{10,32}"""),
		),
	dtypes.RePatternDict(
		ID='stripe-secret-token',
		Title='Stripe Secret Key',
		Severity='CRITICAL',
		Regex=re.compile(r"""(?i)sk_(test|live)_[0-9a-z]{10,32}"""),
		),
	dtypes.RePatternDict(
		ID='pypi-upload-token',
		Title='PyPI upload token',
		Severity='HIGH',
		Regex=re.compile(r"""pypi-AgEIcHlwaS5vcmc[A-Za-z0-9\-_]{50,1000}"""),
		),
	dtypes.RePatternDict(
		ID='gcp-service-account',
		Title='Google (GCP) Service-account',
		Severity='CRITICAL',
		Regex=re.compile(r"""\"type\": \"service_account\""""),
		),
	dtypes.RePatternDict(
		ID='heroku-api-key',
		Title='Heroku API Key',
		Severity='HIGH',
		Regex=re.compile(r"""(?i)(?P<key>heroku[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='slack-web-hook',
		Title='Slack Webhook',
		Severity='MEDIUM',
		Regex=re.compile(r"""https:\/\/hooks\.slack\.com\/services\/[A-Za-z0-9+\/]{44,48}"""),
		),
	dtypes.RePatternDict(
		ID='twilio-api-key',
		Title='Twilio API Key',
		Severity='MEDIUM',
		Regex=re.compile(r"""SK[0-9a-fA-F]{32}"""),
		),
	dtypes.RePatternDict(
		ID='age-secret-key',
		Title='Age secret key',
		Severity='MEDIUM',
		Regex=re.compile(r"""AGE-SECRET-KEY-1[QPZRY9X8GF2TVDW0S3JN54KHCE6MUA7L]{58}"""),
		),
	dtypes.RePatternDict(
		ID='facebook-token',
		Title='Facebook token',
		Severity='LOW',
		Regex=re.compile(r"""(?i)(?P<key>facebook[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-f0-9]{32})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='twitter-token',
		Title='Twitter token',
		Severity='LOW',
		Regex=re.compile(r"""(?i)(?P<key>twitter[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-f0-9]{35,44})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='adobe-client-id',
		Title='Adobe Client ID (Oauth Web)',
		Severity='LOW',
		Regex=re.compile(r"""(?i)(?P<key>adobe[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-f0-9]{32})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='adobe-client-secret',
		Title='Adobe Client Secret',
		Severity='LOW',
		Regex=re.compile(r"""(?i)(p8e-)[a-z0-9]{32}"""),
		),
	dtypes.RePatternDict(
		ID='alibaba-access-key-id',
		Title='Alibaba AccessKey ID',
		Severity='HIGH',
		Regex=re.compile(r"""(?i)([^0-9A-Za-z]|^)(?P<secret>(LTAI)[a-z0-9]{20})([^0-9A-Za-z]|$)"""),
		),
	dtypes.RePatternDict(
		ID='alibaba-secret-key',
		Title='Alibaba Secret Key',
		Severity='HIGH',
		Regex=re.compile(r"""(?i)(?P<key>alibaba[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-z0-9]{30})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='asana-client-id',
		Title='Asana Client ID',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(?P<key>asana[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[0-9]{16})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='asana-client-secret',
		Title='Asana Client Secret',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(?P<key>asana[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-z0-9]{32})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='atlassian-api-token',
		Title='Atlassian API token',
		Severity='HIGH',
		Regex=re.compile(r"""(?i)(?P<key>atlassian[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-z0-9]{24})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='bitbucket-client-id',
		Title='Bitbucket client ID',
		Severity='HIGH',
		Regex=re.compile(r"""(?i)(?P<key>bitbucket[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-z0-9]{32})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='bitbucket-client-secret',
		Title='Bitbucket client secret',
		Severity='HIGH',
		Regex=re.compile(r"""(?i)(?P<key>bitbucket[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-z0-9_\-]{64})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='beamer-api-token',
		Title='Beamer API token',
		Severity='LOW',
		Regex=re.compile(r"""(?i)(?P<key>beamer[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>b_[a-z0-9=_\-]{44})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='clojars-api-token',
		Title='Clojars API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(CLOJARS_)[a-z0-9]{60}"""),
		),
	dtypes.RePatternDict(
		ID='contentful-delivery-api-token',
		Title='Contentful delivery API token',
		Severity='LOW',
		Regex=re.compile(r"""(?i)(?P<key>contentful[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-z0-9\-=_]{43})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='databricks-api-token',
		Title='Databricks API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""dapi[a-h0-9]{32}"""),
		),
	dtypes.RePatternDict(
		ID='discord-api-token',
		Title='Discord API key',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(?P<key>discord[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-h0-9]{64})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='discord-client-id',
		Title='Discord client ID',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(?P<key>discord[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[0-9]{18})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='discord-client-secret',
		Title='Discord client secret',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(?P<key>discord[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-z0-9=_\-]{32})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='doppler-api-token',
		Title='Doppler API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)['\"](dp\.pt\.)[a-z0-9]{43}['\"]"""),
		),
	dtypes.RePatternDict(
		ID='dropbox-api-secret',
		Title='Dropbox API secret/key',
		Severity='HIGH',
		Regex=re.compile(r"""(?i)(dropbox[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"]([a-z0-9]{15})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='dropbox-short-lived-api-token',
		Title='Dropbox short lived API token',
		Severity='HIGH',
		Regex=re.compile(r"""(?i)(dropbox[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](sl\.[a-z0-9\-=_]{135})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='dropbox-long-lived-api-token',
		Title='Dropbox long lived API token',
		Severity='HIGH',
		Regex=re.compile(r"""(?i)(dropbox[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"][a-z0-9]{11}(AAAAAAAAAA)[a-z0-9\-_=]{43}['\"]"""),
		),
	dtypes.RePatternDict(
		ID='duffel-api-token',
		Title='Duffel API token',
		Severity='LOW',
		Regex=re.compile(r"""(?i)['\"]duffel_(test|live)_[a-z0-9_-]{43}['\"]"""),
		),
	dtypes.RePatternDict(
		ID='dynatrace-api-token',
		Title='Dynatrace API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)['\"]dt0c01\.[a-z0-9]{24}\.[a-z0-9]{64}['\"]"""),
		),
	dtypes.RePatternDict(
		ID='easypost-api-token',
		Title='EasyPost API token',
		Severity='LOW',
		Regex=re.compile(r"""(?i)['\"]EZ[AT]K[a-z0-9]{54}['\"]"""),
		),
	dtypes.RePatternDict(
		ID='fastly-api-token',
		Title='Fastly API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(?P<key>fastly[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-z0-9\-=_]{32})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='finicity-client-secret',
		Title='Finicity client secret',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(?P<key>finicity[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-z0-9]{20})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='finicity-api-token',
		Title='Finicity API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(?P<key>finicity[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-f0-9]{32})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='flutterwave-public-key',
		Title='Flutterwave public/secret key',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)FLW(PUB|SEC)K_TEST-[a-h0-9]{32}-X"""),
		),
	dtypes.RePatternDict(
		ID='flutterwave-enc-key',
		Title='Flutterwave encrypted key',
		Severity='MEDIUM',
		Regex=re.compile(r"""FLWSECK_TEST[a-h0-9]{12}"""),
		),
	dtypes.RePatternDict(
		ID='frameio-api-token',
		Title='Frame.io API token',
		Severity='LOW',
		Regex=re.compile(r"""(?i)fio-u-[a-z0-9\-_=]{64}"""),
		),
	dtypes.RePatternDict(
		ID='gocardless-api-token',
		Title='GoCardless API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)['\"]live_[a-z0-9\-_=]{40}['\"]"""),
		),
	dtypes.RePatternDict(
		ID='grafana-api-token',
		Title='Grafana API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)['\"]eyJrIjoi[a-z0-9\-_=]{72,92}['\"]"""),
		),
	dtypes.RePatternDict(
		ID='hashicorp-tf-api-token',
		Title='HashiCorp Terraform user/org API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)['\"][a-z0-9]{14}\.atlasv1\.[a-z0-9\-_=]{60,70}['\"]"""),
		),
	dtypes.RePatternDict(
		ID='hubspot-api-token',
		Title='HubSpot API token',
		Severity='LOW',
		Regex=re.compile(r"""(?i)(?P<key>hubspot[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-h0-9]{8}-[a-h0-9]{4}-[a-h0-9]{4}-[a-h0-9]{4}-[a-h0-9]{12})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='intercom-api-token',
		Title='Intercom API token',
		Severity='LOW',
		Regex=re.compile(r"""(?i)(?P<key>intercom[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-z0-9=_]{60})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='intercom-client-secret',
		Title='Intercom client secret/ID',
		Severity='LOW',
		Regex=re.compile(r"""(?i)(?P<key>intercom[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-h0-9]{8}-[a-h0-9]{4}-[a-h0-9]{4}-[a-h0-9]{4}-[a-h0-9]{12})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='ionic-api-token',
		Title='Ionic API token',
        Severity='LOW',
		Regex=re.compile(r"""(?i)(ionic[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](ion_[a-z0-9]{42})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='jwt-token',
		Title='JWT token',
		Severity='MEDIUM',
		Regex=re.compile(r"""ey[a-zA-Z0-9]{17,}\.ey[a-zA-Z0-9\/\\_-]{17,}\.(?:[a-zA-Z0-9\/\\_-]{10,}={0,2})?"""),
		),
	dtypes.RePatternDict(
		ID='linear-api-token',
		Title='Linear API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)lin_api_[a-z0-9]{40}"""),
		),
	dtypes.RePatternDict(
		ID='linear-client-secret',
		Title='Linear client secret/ID',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(?P<key>linear[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-f0-9]{32})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='lob-api-key',
		Title='Lob API Key',
		Severity='LOW',
		Regex=re.compile(r"""(?i)(?P<key>lob[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>(live|test)_[a-f0-9]{35})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='lob-pub-api-key',
		Title='Lob Publishable API Key',
		Severity='LOW',
		Regex=re.compile(r"""(?i)(?P<key>lob[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>(test|live)_pub_[a-f0-9]{31})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='mailchimp-api-key',
		Title='Mailchimp API key',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(?P<key>mailchimp[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-f0-9]{32}-us20)['\"]"""),
		),
	dtypes.RePatternDict(
		ID='mailgun-token',
		Title='Mailgun private API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(?P<key>mailgun[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>(pub)?key-[a-f0-9]{32})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='mailgun-signing-key',
		Title='Mailgun webhook signing key',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(?P<key>mailgun[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-h0-9]{32}-[a-h0-9]{8}-[a-h0-9]{8})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='mapbox-api-token',
		Title='Mapbox API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(pk\.[a-z0-9]{60}\.[a-z0-9]{22})"""),
		),
	dtypes.RePatternDict(
		ID='messagebird-api-token',
		Title='MessageBird API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(?P<key>messagebird[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-z0-9]{25})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='messagebird-client-id',
		Title='MessageBird API client ID',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(?P<key>messagebird[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-h0-9]{8}-[a-h0-9]{4}-[a-h0-9]{4}-[a-h0-9]{4}-[a-h0-9]{12})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='new-relic-user-api-key',
		Title='New Relic user API Key',
		Severity='MEDIUM',
		Regex=re.compile(r"""['\"](NRAK-[A-Z0-9]{27})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='new-relic-user-api-id',
		Title='New Relic user API ID',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)(?P<key>newrelic[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[A-Z0-9]{64})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='new-relic-browser-api-token',
		Title='New Relic ingest browser API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""['\"](NRJS-[a-f0-9]{19})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='npm-access-token',
		Title='npm access token',
		Severity='CRITICAL',
		Regex=re.compile(r"""(?i)['\"](npm_[a-z0-9]{36})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='planetscale-password',
		Title='PlanetScale password',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)pscale_pw_[a-z0-9\-_\.]{43}"""),
		),
	dtypes.RePatternDict(
		ID='planetscale-api-token',
		Title='PlanetScale API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)pscale_tkn_[a-z0-9\-_\.]{43}"""),
		),
	dtypes.RePatternDict(
		ID='postman-api-token',
		Title='Postman API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)PMAK-[a-f0-9]{24}\-[a-f0-9]{34}"""),
		),
	dtypes.RePatternDict(
		ID='pulumi-api-token',
		Title='Pulumi API token',
		Severity='HIGH',
		Regex=re.compile(r"""pul-[a-f0-9]{40}"""),
		),
	dtypes.RePatternDict(
		ID='rubygems-api-token',
		Title='Rubygem API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""rubygems_[a-f0-9]{48}"""),
		),
	dtypes.RePatternDict(
		ID='sendgrid-api-token',
		Title='SendGrid API token',
		Severity='MEDIUM',
		Regex=re.compile(r"""(?i)SG\.[a-z0-9_\-\.]{66}"""),
		),
	dtypes.RePatternDict(
		ID='sendinblue-api-token',
		Title='Sendinblue API token',
		Severity='LOW',
		Regex=re.compile(r"""(?i)xkeysib-[a-f0-9]{64}\-[a-z0-9]{16}"""),
		),
	dtypes.RePatternDict(
		ID='shippo-api-token',
		Title='Shippo API token',
		Severity='LOW',
		Regex=re.compile(r"""shippo_(live|test)_[a-f0-9]{40}"""),
		),
	dtypes.RePatternDict(
		ID='linkedin-client-secret',
		Title='LinkedIn Client secret',
		Severity='LOW',
		Regex=re.compile(r"""(?i)(?P<key>linkedin[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-z]{16})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='linkedin-client-id',
		Title='LinkedIn Client ID',
		Severity='LOW',
		Regex=re.compile(r"""(?i)(?P<key>linkedin[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-z0-9]{14})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='twitch-api-token',
		Title='Twitch API token',
		Severity='LOW',
		Regex=re.compile(r"""(?i)(?P<key>twitch[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"](?P<secret>[a-z0-9]{30})['\"]"""),
		),
	dtypes.RePatternDict(
		ID='typeform-api-token',
		Title='Typeform API token',
		Severity='LOW',
		Regex=re.compile(r"""(?i)(?P<key>typeform[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}(?P<secret>tfp_[a-z0-9\-_\.=]{59})"""),
		),
	dtypes.RePatternDict(
		ID='dockerconfig-secret',
		Title='Dockerconfig secret exposed',
		Severity='HIGH',
		Regex=re.compile(r"""(?i)(\.(dockerconfigjson|dockercfg):\s*\|*\s*(?P<secret>(ey|ew)+[A-Za-z0-9\/\+=]+))"""),
		),
	]
