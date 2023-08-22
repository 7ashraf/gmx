using DataStore as ds;
methods {
    // DataStore
    function _.getUint(bytes32) external => DISPATCHER(true);
    function _.getAddress(bytes32) external => DISPATCHER(true);
    function _.getBytes32(bytes32) external => DISPATCHER(true);
    // RoleStore
    function _.hasRole(address,bytes32) external => DISPATCHER(true);
    // OracleStore
    function _.getSigner(uint256) external => DISPATCHER(true);
    // PriceFeed
    function _.latestRoundData() external => DISPATCHER(true);
    /// Chain
    function _.arbBlockNumber() external => ghostBlockNumber() expect uint256 ALL;
    function _.arbBlockHash(uint256 blockNumber) external => ghostBlockHash(blockNumber) expect bytes32 ALL;
    /// Oracle summaries
    function Oracle._getSalt() internal returns bytes32 => mySalt();

    /// Getters:
    function OracleHarness.primaryPrices(address) external returns (uint256,uint256);
    function OracleHarness.secondaryPrices(address) external returns (uint256,uint256);
    function OracleHarness.customPrices(address) external returns (uint256,uint256);
    function OracleHarness.getSignerByInfo(uint256, uint256) external returns (address);
    function getTokensWithPrices(uint256, uint256) external  returns (address[] memory);
    function getPriceFeedPrice(address dataStore, address token) external returns ( uint256);
    function getPrimaryPrice(address token) external  returns (Price.Props memory);
    function getTokensWithPricesCount() external  returns (uint256);
    function clearAllPrices() external;
    function getPrimaryPrice(address token) external returns (Price.Props memory);
    function OracleHarness.etPriceFeedMultiplier(address dataStore, address token) external returns (uint256);
}

ghost mySalt() returns bytes32;

ghost ghostBlockNumber() returns uint256 {
    axiom ghostBlockNumber() !=0;
}

ghost ghostBlockHash(uint256) returns bytes32 {
    axiom forall uint256 num1. forall uint256 num2. 
        num1 != num2 => ghostBlockHash(num1) != ghostBlockHash(num2);
}

function ghostMedian(uint256[] array) returns uint256 {
    uint256 med;
    uint256 len = array.length;
    require med >= array[0] && med <= array[require_uint256(len-1)];
    return med;
}

rule sanity_satisfy(method f) {
    env e;
    calldataarg args;
    f(e, args);
    satisfy true;
}

rule validateSignerConsistency() {
    env e1; env e2;
    require e1.msg.value == e2.msg.value;
    
    bytes32 salt1;
    bytes32 salt2;
    address signer1;
    address signer2;
    bytes signature;

    validateSignerHarness(e1, salt1, signature, signer1);
    validateSignerHarness@withrevert(e2, salt2, signature, signer2);

    assert (salt1 == salt2 && signer1 == signer2) => !lastReverted,
        "Revert characteristics of validateSigner are not consistent";
}

rule _getPriceFeedPriceSpec{
    address dataStore;
    address token;
    env e;


    uint256 price = getPriceFeedPrice(e, dataStore, token);

    //assert price != 0;

    assert price > 0;
    //satisfy price == 0;

}

rule clearAllPricesSpec{
    env e;
    uint i;
    uint256 maxBoundBefore = getTokensWithPricesCount(e);
    address[] tokenWithPricesBefore = getTokensWithPrices(e,0, maxBoundBefore);
    address token;
    Price.Props propsBefore = getPrimaryPrice(e,token);
    //(uint256 minBefore, uint256 maxBefore) = getPrimaryPrice(e,token);

    clearAllPrices(e);

    uint256 maxBound = getTokensWithPricesCount(e);
    address[] tokenWithPrices = getTokensWithPrices(e,0, maxBound);
    Price.Props props = getPrimaryPrice(e,token);
    uint256 min = props.min;
    uint256 max = props.max;
    //(uint256 min, uint256 max) = getPrimaryPrice(e, token);
    
    //assert min ==0;
    //assert max ==0;
    assert i >=0 && i<maxBound => tokenWithPrices[i] == 0;
    

}

rule getPrimaryPrice{
    address token;
    env e;

    Price.Props props = getPrimaryPrice(e, token);

    mathint min = props.min;
    mathint max = props.max;


    assert token == 0 => min == 0 && max == 0;
    assert token != 0 => min > 0 && max > 0;


}

rule getPriceFeedMultiplier{

    env e;
    address dataStore;
    address token;

    uint256 mult = getPriceFeedMultiplier(e, dataStore, token);

    assert mult > 0;
}