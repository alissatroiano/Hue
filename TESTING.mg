# TESTING.md

## Front-End Tests

### HTML

#### LOGIN PAGE

	***- Login Page Test #1:***
		- 1. Copy the contents of `login.html` to clipboard.
		- 2. Visit [W3 Validator](https://validator.w3.org/nu/#textarea).
		- 3. Paste the content from clipboard into the validator and submit the form.
		- 4. Observe several warnings caused by code written in Django's templating language.
		- 5. Observe a few small errors, including:
			- Duplicate id used on 2 fields in the login form.
			- Incorrect placement of the `placeholder` attribute. 