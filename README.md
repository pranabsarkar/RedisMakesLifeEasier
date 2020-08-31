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
present, else `None`. Here, the details will be stored in JSON list Data Structure.

3. If the response for the quried data form Redis DB is `None`, the response from
SQLite Database will be returned back to the Compute Engine with updating the Key 
in the Redis DB.


### Sample - Payload

* REQUEST: `POST`
* URL: `http://127.0.0.1:5000/v1`

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

`git clone https://github.com/pranabsarkar/RedisLovesSQLite.git`

Once, it is cloned run-

`cd RedisLovesSQLite`

Please open terminal in the current directory and run this command to insatall the dependencies-

`pip install -r requirements.txt`

Open terminal and run this command to start the server -

`python app.py `

## Reference

1. [Redis Documentation](https://redis.io/topics/quickstart)

## Author

* Name: Pranab Sarkar
* LinkedIN: http://bit.ly/pzlinked
* Email-ID: sarkarpranab66@gmail.com
