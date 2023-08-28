methods {
    // RoleStore.sol
    function _.hasRole(address, bytes32) external => DISPATCHER(true);

    function applyDeltaToUint(bytes32 key, int256 value, string memory errorMessage) external returns (uint256);
    function getUint(bytes32 key) external returns (uint256);
    function getInt(bytes32 key) external returns (int256);
    function applyBoundedDeltaToUint(bytes32 key, int256 value) external returns (uint256);
    function incrementInt(bytes32 key, int256 value) external  returns (int256);
    function decrementInt(bytes32 key, int256 value) external  returns (int256);
    function incrementUint(bytes32 key, uint256 value) external  returns (uint256);
    function decrementUint(bytes32 key, uint256 value) external  returns (uint256);
}

rule incrementIntSpec{
    env e;
    bytes32 key;
    int256 incValue;

    int256 prevValue = getInt(e, key);
    int256 newValue = incrementInt(e, key, incValue);

    assert prevValue <= newValue;
    assert newValue == assert_int256(prevValue + incValue);

}
rule decrementIntSpec{
    
    env e;
    bytes32 key;
    int256 decValue;

    int256 prevValue = getInt(e, key);
    int256 newValue = decrementInt(e, key, decValue);

    assert prevValue >= newValue;
    assert newValue == assert_int256(prevValue - decValue);
}
