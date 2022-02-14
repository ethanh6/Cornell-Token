// contracts/OurToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract CornellToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("CornellToken", "CT") {
        _mint(msg.sender, initialSupply);
    }
}
