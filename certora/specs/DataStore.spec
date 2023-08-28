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

rule sanity_satisfy(method f) {
    env e;
    calldataarg args;
    f(e, args);
    satisfy true;
}

rule applyDeltaToUintSpec{

    bytes32 key;
    int256 addedValue;
    string errorMessage = "errorMessage";
    env e;

    uint256 value = getUint(e, key);
    require value != 0;
    require addedValue !=0;
    mathint realResult = value + addedValue;
    mathint expectedResult = applyDeltaToUint(e, key, addedValue, errorMessage);

   // assert realResult == expectedResult;

    //check that it is possible for result to be greater than or equal 0
    assert expectedResult != 0;

    //assert result is real


   


}

rule applyBoundedDeltaToUintSpec{
    env e;
    bytes32 key;
    int256 value;

    uint256 prev = getUint(e, key);
    mathint expectedResult = prev + value;

    mathint result = applyBoundedDeltaToUint(e, key, value);


    assert result >= 0;
    assert result == expectedResult;
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

rule incrementUintSpec{
    env e;
    bytes32 key;
    uint256 incValue;

    uint256 prevValue = getUint(e, key);
    uint256 newValue = incrementUint(e, key, incValue);

    assert prevValue <= newValue;
    assert newValue == assert_uint256(prevValue + incValue);

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

rule decrementUintSpec{
    
    env e;
    bytes32 key;
    uint256 decValue;

    uint256 prevValue = getUint(e, key);
    uint256 newValue = decrementUint(e, key, decValue);

    assert prevValue >= newValue;
    assert newValue == assert_uint256(prevValue - decValue);

}