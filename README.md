# RedisMakesLifeEasier

## Technical Blog

In this blog you can check some more details on Redis implementation - [Medium Blog](https://medium.com/@sarkarpranab66/implementing-redis-cache-within-aws-lambda-function-for-better-response-latency-part-1-overview-19da1e5369ef).

## Overview

Here, we can get the details of every registered Photographers for the
queried zip code, who are using a specific product.

This is a simple Python Based Template where we can leverage the 
benfits of Redis over using a Regular Database in the Cloud.

![Architecture-Overview](/docs/redislovesdb.png)

## Steps - Involved

1. The Compute Engine (EC2) recives an request from the API Gateway to
query photographers in a particular ZIP code, who are using a specific product.

2. The Redis in memory database will return the details if the queried key is
present, else `None`. Here, the details will be stored in JSON list Data Structure.

3. If the response for the queried data form Redis DB is `None`, the response from
SQLite Database will be returned back to the Compute Engine with updating the Key 
in Redis DB.


### Sample - Payload

* REQUEST: `POST`
* URL: `http://127.0.0.1:5001/v1`

```JSON

{
    "zipcode": "855058",
    "product-name": "ABC"
}

```

### Sample - Response

```JSON

{
    "data": [
        {
            "contact": "232-568-8464",
            "name": "Charity",
            "email": "cthynnea@gnu.org",
            "zipcode": "855058",
            "id": 2
        }
    ]
}

```

## Testing

Will be added soon.

## Setup Guide

First of all, clone this using terminal after running-

`git clone https://github.com/pranabsarkar/RedisMakesLifeEasier.git`

Once, it is cloned run-

`cd RedisMakesLifeEasier`

Please open terminal in the current directory and run this command to insatall the dependencies-

`pip install -r requirements.txt`

Open terminal and run this command to start the server -

`python app.py `

## Reference

1. [Redis Documentation](https://redis.io/topics/quickstart)

## Author

Name: Pranab Sarkar

Please feel free to add your input's :)
