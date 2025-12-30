- They manually coded JDBC for database access
- Created their own thread pools for concurrency
	- Thread pool managed by 'container'
		- what does 'container' mean here?
	- so now you can write and manage by code
		- back then it was invisible in your code
- Implemented custom transaction management
	- before EJB you wrote all code manually (rollbacks etc.)
	- after EJB: just add `@TransactionAttribute`; as well, it supported distributed transactions and 2PC.
- Built Security frameworks
	- custom interceptors, user/role tables, auth filters, authz checks
	- hardcoded `if (user.hasRole("ADMIN"))`
		- after EJB, you just use `@RolesAllowed("ADMIN")`


## Every company reinvented the wheel

> All these codes are considered as **infrastructure code**
> Because they don't solve **business problems**

writing thousands of lines of complex infrastructure code before even starting on business logic.
