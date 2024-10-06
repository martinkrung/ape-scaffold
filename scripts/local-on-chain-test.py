#!/usr/bin/env python3

import os
import sys
import boa


RPC_ETHEREUM = os.getenv('RPC_ETHEREUM')
RPC_ARBITRUM = os.getenv('RPC_ARBITRUM')
ARBISCAN_API_KEY = os.getenv('ARBISCAN_API_KEY')
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')
DEPLOYED_CONTRACT = os.getenv('DEPLOYED_CONTRACT')

boa.env.fork(RPC_ARBITRUM)

MIN_RATE = int(.01 * 1e18 / (365 * 86400))
MAX_RATE = int(.25 * 1e18 / (365 * 86400))

deployed_contract = boa.from_etherscan(
    DEPLOYED_CONTRACT,
    name="Contract",
    uri="https://api.arbiscan.io/api",
    api_key=ARBISCAN_API_KEY
)


test = deployed_contract.function(arg1, arg2)

local_place_holder = boa.load("../contracts/PlaceHolder.vy", arg1, arg2)

test = local_place_holder.function(arg1, arg2)
print(f"test: {test}")

assert test == "test", "Test failed"

#with boa.env.prank(CONTROLLER_ADDRESS):
 #   rate = rate * 365 * 86400
  #  print(f"rate: {rate}")
   # print(f"rate: {rate / 10**18}")

