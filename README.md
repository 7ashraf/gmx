
# Navigating Software Reliability: My Formal Verification Odyssey with Certora Verification Language

## Introduction

In the realm of software development, precision matters. This document chronicles my journey in a contest where I harnessed the Certora Verification Language to ensure software correctness.

Certora Verification Language acts as a translator between software and mathematical validation. This document outlines my verification methods, detailing strategies, Certora tools, code insights, challenges, and outcomes.

My goal in sharing this experience is to underscore the potency of formal verification and inspire others in the software world to explore its application. Join me as we delve into the role of Certora in achieving dependable code and ushering in an era of trustworthy software systems.

## Problem Statement

In the context of the gmx-formal-verification contest on Code4Arena, my mission was to use formal verification techniques to scrutinize code accuracy. I followed this approach:

1. Confirming input and output compliance with rules.
2. Identifying peculiar scenarios.
3. Validating logical behavior in the code.
4. Investigating conditional statements that trigger transaction reversals.

## Verification Methods

For each problem addressed, I adhered to this structure:

1. **Method Description**
2. **Verification Strategy**
3. **Utilized Certora Constructs**
4. **Code Explanation**
5. **Overcoming Challenges**
6. **Final Outcomes**

Next, I'll elaborate on the Certora rules employed, elucidate anticipated function logic and behavior, touch on exceptional scenarios and limitations, and substantiate how the rules formally ensure method efficacy.

## Methods for Formal Verification

### DataStore.sol

#### applyDeltaToUint

**Method Description:** This function alters a stored numerical value.

**Verification Strategy:** Validate non-zero result and non-negative value.

**Certora Constructs Used:** applyDeltaToUintSpec

**Code Explanation:** The rule confirms the result is positive.

### applyBoundedDeltaToUint

**Method Description:** This function alters a stored number.

**Verification Strategy:** Ensure non-negative number and, if input is negative, result must be zero.

**Certora Constructs Used:** applyBoundedDeltaToUintSpec

**Code Explanation:** This rule assures that the value increases and is accurately set.

### incrementInt

**Method Description:** Amplify a number by a specified value.

**Verification Strategy:** Verify result is higher than the initial value.

**Certora Constructs Used:** incrementIntSpec
**Issue**: incrementInt
**Summary**: the function allows incrementing by a negative value, thus giving anomaly behaviour

**Code Explanation:** Rules validate that the new value increases and is in line with summation.

### decrementInt

**Method Description:** Diminish a number by a specified value.

**Verification Strategy:** Ascertain result is lower than the initial value.

**Certora Constructs Used:** decrementIntSpec

**Code Explanation:** The rule affirms the expected reduction in number.
**Issue**: decrementInt
**Summary**: the function allows decrementing by a negative value, thus giving anomaly behaviour
### incrementUint

**Method Description:** Amplify a number by a specified value.

**Verification Strategy:** Verify result is higher than the initial value.

**Certora Constructs Used:** incrementUintSpec
### decrementUint

**Method Description:** Diminish a number by a specified value.

**Verification Strategy:** Ascertain result is lower than the initial value.

**Certora Constructs Used:** decrementUintSpec

**Code Explanation:** The rule affirms the expected reduction in number.

### _getPriceFeedPrice

**Method Description:** Calculate and return a computed price.

**Verification Strategy:** Validate non-negative, non-zero price.

**Certora Constructs Used:** _getPriceFeedPriceSpec

**Code Explanation:** Certora rules confirm price positivity and non-zero nature.

### clearAllPrices

**Method Description:** Delete token prices via a loop.

**Verification Strategy:** Confirm tokens and associated prices are deleted.

**Certora Constructs Used:** clearAllPricesSpec

**Code Explanation:** Rules validate empty array and clearance of Price.Props structure.
**Issue**: clearAllPrices
**Summary**: the function doesn't use the counter i created in the for loop to loop on the array, thus deleting nothing but the first index

### getPrimaryPrice

**Method Description:** Retrieve a primary price.

**Verification Strategy:** Validate token validity and handling of zero tokens.

**Certora Constructs Used:** getPrimaryPriceSpec

**Code Explanation:** Rules confirm valid tokens and handle cases when tokens are zero.

### getPriceFeedMultiplier

**Method Description:** Retrieve a multiplier from storage.

**Verification Strategy:** Confirm multiplier is non-zero.

**Certora Constructs Used:** getPriceFeedMultiplierSpec

**Code Explanation:** Rules ensure multiplier's positivity.

### syncTokenBalance

**Method Description:** Synchronize stored balances with actual balances.

**Verification Strategy:** Verify parity between stored and actual balances.

**Certora Constructs Used:** syncTokenBalanceSpec

**Code Explanation:** Rule confirms equality between stored and actual balances.

### recordTransferIn

**Method Description:** Log incoming transfers.

**Verification Strategy:** Validate accurate recording of balance changes.

**Certora Constructs Used:** recordTransferInSpec

**Code Explanation:** Rules ensure that stored balances reflect real changes.

### afterTransferOut

**Method Description:** Update balances post-transfer.

**Verification Strategy:** Validate correct update of balances.

**Certora Constructs Used:** afterTransferOutSpec

**Code Explanation:** Rules confirm proper update of stored balances.

By methodically verifying each function, its logic, and behavior, Certora bolsters the reliability of software. This journey encountered challenges but proved enlightening, unveiling valuable insights and best practices.

## Conclusion

My exploration of formal verification through Certora has underscored the potential for building dependable software systems. By sharing my journey and lessons learned, I hope to inspire a wider embrace of formal verification methodologies. This document serves as a testament to the power of Certora Verification Language in enhancing software reliability.



## Contact Information

If you have any questions or would like to discuss formal verification further, feel free to reach out:

- Email: [muhamed.ashrafahmed@gmail.com](mailto:muhamed.ashrafahmed@gmail.com)
- GitHub: [@7ashraf](https://github.com/7ashraf)

Thank you for joining me on this journey of software reliability!

---
*Document written by Mohamed Ashraf*

*Last updated: 28/08/2023*
