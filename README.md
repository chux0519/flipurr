# flipurr

fetch image from flickr, then use [purrmitive](https://github.com/chux0519/purr/tree/master/purrmitive) to generate an output and publish to your social network.

## supported social networks

- mastodon
- quorum groups

## requirements

- flickr API key and secret
- [purr](https://github.com/chux0519/purr/tree/master/purrmitive) binary
- social network credentials
  - mastodon: you need user name and password
  - quorum groups: you need a quorum API server, and the JWT and TLS certs of it.

## usage

env

```
export MASTODON_USER_NAME=''
export MASTODON_PASSWORD=''
export USER_SECRET_FILE='/home/xxx//purrbot_usercred.secret'
export APP_SECRET_FILE='/home/xxx/purrbot_clientcred.secret'
export FLICKR_API_KEY=''
export FLICKR_API_SECRET=''
export QUORUM_API_BASE_URL='https://xxx.xxx.xxx.xxx:8000'
export QUORUM_GROUP_ID=''
export QUORUM_API_JWT=''
```

