// SPDX-License-Identifier: BUSL-1.1
pragma solidity ^0.8.0;

import "../../contracts/role/RoleStore.sol";
contract RoleStoreHarness is RoleStore {
    

    function getControllerRole() pure external returns (bytes32) {
        return 0x97adf037b2472f4a6a9825eff7d2dd45e37f2dc308df2a260d6a72af4189a65b;
    }

    
    
}
