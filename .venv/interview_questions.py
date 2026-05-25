# Function that reverses a string
def reverse_string('grasshopper'):
    return ''.join(reversed('grasshopper'))


# Test. Verification of reverse_string function
def test_reverse_string():
    input_str = "grasshopper"

    # Perform the reverse operation
    reversed_str = reverse_string(input_str)

    # Check if the reversed string matches the expected output
    assert reversed_str == "reppohssarg"

    print("Test Passed! " + input_str + "'s reverse is " + reversed_str)