methods {
    // ERC20
    function _.name()                                external  => DISPATCHER(true);
    function _.symbol()                              external  => DISPATCHER(true);
    function _.decimals()                            external  => DISPATCHER(true);
    function _.totalSupply()                         external  => DISPATCHER(true);
    function _.balanceOf(address)                    external  => DISPATCHER(true);
    function _.allowance(address,address)            external  => DISPATCHER(true);
    function _.approve(address,uint256)              external  => DISPATCHER(true);
    function _.transfer(address,uint256)             external  => DISPATCHER(true);
    function _.transferFrom(address,address,uint256) external  => DISPATCHER(true);

    // DataStore
    function _.getUint(bytes32) external => DISPATCHER(true);
    function _.getAddress(bytes32) external => DISPATCHER(true);
    function _.getBytes32(bytes32) external => DISPATCHER(true);
    // RoleStore
    function _.hasRole(address,bytes32) external => DISPATCHER(true);

    // WNT
    function _.deposit()                             external  => DISPATCHER(true);
    function _.withdraw(uint256)                     external  => DISPATCHER(true);

    function tokenBalances(address) external returns (uint256) envfree;
    function recordTransferIn(address token) external returns (uint256);
    function StrictBank.afterTransferOut(address token) external;
    //get CONTROLLEr Role
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