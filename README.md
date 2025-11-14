# type_check

<h1>Overview</h1>
The only_ints() function checks whether both parameters provided are integers (int) — returning True if they are, and False otherwise.<br>
It also explicitly filters out boolean values (True or False), since in Python those are technically a subclass of integers.<br>

<h2>How It Works</h2>

<ul>
  <li>The function prints both parameters to show what values are being compared.</li>
  <li>It checks if either parameter is a boolean (True or False):</li>
  <ul>
    <li>If so, it prints "caught true or false value" and returns False immediately.</li>
  </ul>
  <li>Otherwise, it checks each parameter’s type using isinstance(param, int) and stores the results in param1Value and param2Value.</li>
  <li>If both results match (both True), it returns True.</li>
  <li>If either is not an integer, it returns False.</li>
</ul>

<h2>Example</h2>
result = only_ints(5, 10)
print(result)

<h2>Output</h2>
5 and 10
True and True
True
