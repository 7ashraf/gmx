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

rule sanity_satisfy(method f) {
    env e;
    calldataarg args;
    f(e, args);
    satisfy true;
}

// syncTokenBalance, afterTransferOut, and recordTransferIn should not change tokenBalances[token1] where token1 != token2
rule balanceIndependence(method f, env e, address token1, address token2) filtered {
    f -> f.selector == sig:recordTransferIn(address).selector 
        || f.selector == sig:afterTransferOut(address).selector
        || f.selector == sig:syncTokenBalance(address).selector
} {
    uint256 balanceBefore = tokenBalances(token2);

    if (f.selector == sig:recordTransferIn(address).selector) {
        recordTransferIn(e, token1);
    } else if (f.selector == sig:afterTransferOut(address).selector) {
        afterTransferOut(e, token1);
    } else if (f.selector == sig:syncTokenBalance(address).selector) {
        syncTokenBalance(e, token1);
    }

    uint256 balanceAfter = tokenBalances(e, token2); 
    assert (token2 != token1 => balanceBefore == balanceAfter);
}
rule syncTokenBalanceSpec {
    env e;
    address token;
    //require msg.sender hasRole onlyController
    //require(hasRole(e.msg.sender, 0x97adf037b2472f4a6a9825eff7d2dd45e37f2dc308df2a260d6a72af4189a65b);

    //alter the value of the token before checking because it initially zero

    //assert tokenBalances of token == the balance of that token in the IERC20 after calling the syncTokenBalance function
    uint realBalance = syncTokenBalance(e, token);

    uint storedBalance = tokenBalances(token);
    assert (storedBalance == realBalance);


}

rule recordTransferInSpec{
    env e;
    address token;
    mathint prevBalance = tokenBalances(token);

    mathint transferredAmount = recordTransferIn(e, token);
    mathint expectedBalanceAfter = transferredAmount + prevBalance;
    mathint balanceAfter = tokenBalances(token);

    assert balanceAfter == expectedBalanceAfter;
}

rule afterTransferOut{
    address token;
    address bank;
    env e;
    
    afterTransferOut(e, token);

    mathint realValue = syncTokenBalance(e, token);
    mathint expectedValue = tokenBalances(token);


    assert realValue == expectedValue;
}