import json
from web3 import Web3

def getAmountNamesRegistered():
    flare_rpc = 'https://flare-api.flare.network/ext/C/rpc'
    web3 = Web3(Web3.HTTPProvider(flare_rpc))

    abi = json.loads('[{"type":"constructor","stateMutability":"nonpayable","inputs":[{"type":"address","name":"_fns","internalType":"contract IFNS"},{"type":"bytes32","name":"_baseNode","internalType":"bytes32"},{"type":"address","name":"_noNameCollisionsContract","internalType":"contract INoNameCollisions"}]},{"type":"event","name":"Approval","inputs":[{"type":"address","name":"owner","internalType":"address","indexed":true},{"type":"address","name":"approved","internalType":"address","indexed":true},{"type":"uint256","name":"tokenId","internalType":"uint256","indexed":true}],"anonymous":false},{"type":"event","name":"ApprovalForAll","inputs":[{"type":"address","name":"owner","internalType":"address","indexed":true},{"type":"address","name":"operator","internalType":"address","indexed":true},{"type":"bool","name":"approved","internalType":"bool","indexed":false}],"anonymous":false},{"type":"event","name":"ControllerAdded","inputs":[{"type":"address","name":"controller","internalType":"address","indexed":true}],"anonymous":false},{"type":"event","name":"ControllerRemoved","inputs":[{"type":"address","name":"controller","internalType":"address","indexed":true}],"anonymous":false},{"type":"event","name":"NameRegistered","inputs":[{"type":"string","name":"name","internalType":"string","indexed":true},{"type":"uint256","name":"id","internalType":"uint256","indexed":true},{"type":"address","name":"owner","internalType":"address","indexed":true},{"type":"uint256","name":"expires","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"NameRenewed","inputs":[{"type":"uint256","name":"id","internalType":"uint256","indexed":true},{"type":"uint256","name":"expires","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"NewNoNameCollisions","inputs":[{"type":"address","name":"noNameCollisions","internalType":"address","indexed":true}],"anonymous":false},{"type":"event","name":"OwnershipTransferred","inputs":[{"type":"address","name":"previousOwner","internalType":"address","indexed":true},{"type":"address","name":"newOwner","internalType":"address","indexed":true}],"anonymous":false},{"type":"event","name":"ResolverSet","inputs":[{"type":"address","name":"resolver","internalType":"address","indexed":true}],"anonymous":false},{"type":"event","name":"Transfer","inputs":[{"type":"address","name":"from","internalType":"address","indexed":true},{"type":"address","name":"to","internalType":"address","indexed":true},{"type":"uint256","name":"tokenId","internalType":"uint256","indexed":true}],"anonymous":false},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"GRACE_PERIOD","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"addController","inputs":[{"type":"address","name":"controller","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"approve","inputs":[{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"tokenId","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"available","inputs":[{"type":"uint256","name":"id","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"balanceOf","inputs":[{"type":"address","name":"owner","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"bytes32","name":"","internalType":"bytes32"}],"name":"baseNode","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"controllers","inputs":[{"type":"address","name":"","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"expiries","inputs":[{"type":"uint256","name":"","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"contract IFNS"}],"name":"fns","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"getApproved","inputs":[{"type":"uint256","name":"tokenId","internalType":"uint256"}]},{"type":"function","stateMutability":"pure","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"getLabelId","inputs":[{"type":"string","name":"label","internalType":"string"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"isApprovedForAll","inputs":[{"type":"address","name":"owner","internalType":"address"},{"type":"address","name":"operator","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"isNotCollision","inputs":[{"type":"string","name":"name","internalType":"string"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"name","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"nameExpires","inputs":[{"type":"uint256","name":"id","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"contract INoNameCollisions"}],"name":"noNameCollisionsContract","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"owner","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"ownerOf","inputs":[{"type":"uint256","name":"tokenId","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"reclaim","inputs":[{"type":"uint256","name":"id","internalType":"uint256"},{"type":"address","name":"owner","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"register","inputs":[{"type":"string","name":"label","internalType":"string"},{"type":"address","name":"owner","internalType":"address"},{"type":"uint256","name":"duration","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"registerOnly","inputs":[{"type":"string","name":"label","internalType":"string"},{"type":"address","name":"owner","internalType":"address"},{"type":"uint256","name":"duration","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"removeController","inputs":[{"type":"address","name":"controller","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"renew","inputs":[{"type":"uint256","name":"id","internalType":"uint256"},{"type":"uint256","name":"duration","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"renounceOwnership","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"safeTransferFrom","inputs":[{"type":"address","name":"from","internalType":"address"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"tokenId","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"safeTransferFrom","inputs":[{"type":"address","name":"from","internalType":"address"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"tokenId","internalType":"uint256"},{"type":"bytes","name":"data","internalType":"bytes"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setApprovalForAll","inputs":[{"type":"address","name":"operator","internalType":"address"},{"type":"bool","name":"approved","internalType":"bool"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setResolver","inputs":[{"type":"address","name":"resolver","internalType":"address"}]},{"type":"function","stateMutability":"pure","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"supportsInterface","inputs":[{"type":"bytes4","name":"interfaceID","internalType":"bytes4"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"symbol","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"tokenURI","inputs":[{"type":"uint256","name":"tokenId","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"transferFrom","inputs":[{"type":"address","name":"from","internalType":"address"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"tokenId","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"transferOwnership","inputs":[{"type":"address","name":"newOwner","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"updateNoNameCollisionContract","inputs":[{"type":"address","name":"newContract","internalType":"contract INoNameCollisions"}]}]')
    name_wrapper_address = '0xA0A9b5B27D8dd064D0109501c1BFd61da17f2052'
    base_registrar_address = '0x570F7b5F751B50b5B2DFF35d553cE05cB27697a7'

    contract = web3.eth.contract(address=base_registrar_address, abi=abi)

    #need to put .call() at the end to call the smart contract
    total_names = contract.functions.balanceOf(name_wrapper_address).call()

    #convert supply to Wei witch is 18 decimal places)
    print('Total Names: ', total_names)

def changeDiscordChannelName():
    print()

def main():
    getAmountNamesRegistered()
    changeDiscordChannelName()

main()