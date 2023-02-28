import argparse
import os
import sys

parser = argparse.ArgumentParser(
    prog = 'ProgramName',
    description = 'What the program does',
    epilog = 'Text at the bottom of help')

parser.add_argument('--address', default="0x")
parser.add_argument('--eth', default="1.0")
parser.add_argument('--glm', default="1.0")

args = parser.parse_args()
os.environ["ETH_GLM_SEND_TARGET"] = args.address
os.environ["ETH_SEND_AMOUNT"] = args.eth
os.environ["GLM_SEND_AMOUNT"] = args.glm

npx_command_split = "npx hardhat run --network dev scripts/send_eth_and_glms.js"
os.chdir("contracts")
os.system(npx_command_split)

