Here are some unit test cases that can be used to test the "myFunc" function:

1. Test if the function is called when the event is dispatched:

```python
def test_myFunc_called_on_event():
    result = []
    
    def myFunc():
        result.append('myFunc called')
    
    event = Event()
    elem = Mock()
    elem.addEventListener('myevent', myFunc, False)
    elem.dispatchEvent(event)
    
    assert result == ['myFunc called']
```

2. Test if the function is not called when the event is not dispatched:

```python
def test_myFunc_not_called_without_event():
    result = []
    
    def myFunc():
        result.append('myFunc called')
    
    elem = Mock()
    elem.addEventListener('myevent', myFunc, False)
    
    assert result == []
```

3. Test if the function is called multiple times when the event is dispatched multiple times:

```python
def test_myFunc_called_multiple_times():
    result = []
    event = Event()
    
    def myFunc():
        result.append('myFunc called')
    
    elem = Mock()
    elem.addEventListener('myevent', myFunc, False)
    elem.dispatchEvent(event)
    elem.dispatchEvent(event)
    elem.dispatchEvent(event)
    
    assert result == ['myFunc called', 'myFunc called', 'myFunc called']
```

4. Test if the function is called with the correct arguments:

```python
def test_myFunc_called_with_correct_arguments():
    result = []
    event = Event()
    
    def myFunc(e):
        result.append('myFunc called with argument: ' + str(e))
    
    elem = Mock()
    elem.addEventListener('myevent', myFunc, False)
    elem.dispatchEvent(event)
    
    assert result == ['myFunc called with argument: ' + str(event)]
```

Note: In these tests, "Event" and "Mock" are placeholder classes and should be replaced with actual implementations based on the specific requirements of your system.