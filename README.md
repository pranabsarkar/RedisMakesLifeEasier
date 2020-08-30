# RedisLovesSQLite

## Overview

Here, we can get the details of every registered Artist's for the
queried zip code.

This is a simple Python Based Template where we can leverage the 
benfits of Redis over using a Regular Database in the Cloud.

![Architecture-Overview](/docs/redislovesdb.png)

## Steps - Involved

1. The Compute Engine (EC2/Lambda) recives an request from the API Gateway to
query Artist's in a particular ZIP code.

2. The Redis in memory database will return the details if the quried key is
present, else `None`.

3. If the response for the quried data form Redis DB is `None`, the response from
SQLite Database will be returned back to the Compute Engine with updating the Key 
in the Redis DB.

## Testing

## Setup Guide

## Reference

## 
