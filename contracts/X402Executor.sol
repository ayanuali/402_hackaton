// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IERC3009 {
    function transferWithAuthorization(
        address from,
        address to,
        uint256 value,
        uint256 validAfter,
        uint256 validBefore,
        bytes32 nonce,
        uint8 v,
        bytes32 r,
        bytes32 s
    ) external;
}

contract X402Executor {
    address public immutable usdcAddress;

    event X402PaymentExecuted(
        address indexed from,
        address indexed to,
        uint256 amount,
        bytes32 nonce
    );

    constructor(address _usdcAddress) {
        usdcAddress = _usdcAddress;
    }

    function executeX402Payment(
        address from,
        address to,
        uint256 amount,
        uint256 validAfter,
        uint256 validBefore,
        bytes32 nonce,
        bytes memory signature
    ) external {
        require(block.timestamp >= validAfter, "Not valid yet");
        require(block.timestamp <= validBefore, "Expired");

        (uint8 v, bytes32 r, bytes32 s) = splitSignature(signature);

        IERC3009(usdcAddress).transferWithAuthorization(
            from,
            to,
            amount,
            validAfter,
            validBefore,
            nonce,
            v,
            r,
            s
        );

        emit X402PaymentExecuted(from, to, amount, nonce);
    }

    function splitSignature(bytes memory sig) internal pure returns (uint8 v, bytes32 r, bytes32 s) {
        require(sig.length == 65, "Invalid signature length");

        assembly {
            r := mload(add(sig, 32))
            s := mload(add(sig, 64))
            v := byte(0, mload(add(sig, 96)))
        }
    }
}
