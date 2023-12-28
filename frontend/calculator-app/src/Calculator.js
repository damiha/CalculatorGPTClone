import React, { useState } from 'react';

const Calculator = () => {
    const calculatorWrapperStyle = {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        height: '100vh',
    };

    const calculatorBoxStyle = {
        display: 'inline-flex',
        flexDirection: 'column',
        alignItems: 'center',
        backgroundColor: 'white',
        borderRadius: '10px',
        border: '2px solid black',
        padding: '20px',
        margin: '0 auto'
    };

    const buttonStyle = {
        width: '60px',
        height: '60px',
        margin: '5px',
        borderRadius: '50%',
        backgroundColor: 'black',
        color: 'white',
        border: '2px solid white',
        fontSize: '20px'
    };

    const equalsButtonStyle = {
        ...buttonStyle,
        backgroundColor: 'orange'
    };

    const displayStyle = {
        width: '280px',
        backgroundColor: 'black',
        color: 'white',
        textAlign: 'right',
        padding: '10px',
        borderRadius: '5px',
        marginBottom: '10px'
    };

    const [expressionString, setExpressionString] = useState('');
    const [leftBracketExists, setLeftBracketExists] = useState(false);

    const handleEqualsSignClick = async () => {
        try {
            const response = await fetch('http://localhost:5000/evaluate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ infix_str: expressionString }),
            });
    
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
    
            const data = await response.json();
            setExpressionString(String(data.result)); // Update the expression string with the result
        } catch (error) {
            console.error('Error during POST request:', error);
        }
    };

    const appendToExpression = (value) => {

        if(value == "<"){
            setExpressionString(prev => prev.slice(0, -1));
        }
        else if(value == "( )" && leftBracketExists){
            setExpressionString(prev => prev + ")");
            setLeftBracketExists(false);
        }
        else if(value == "( )" && !leftBracketExists){
            setExpressionString(prev => prev + "(");
            setLeftBracketExists(true);
        }
        else{
            setExpressionString(prev => prev + value);
        }
    };

    return (
        <div style={calculatorWrapperStyle}>
            <div style={calculatorBoxStyle}>
                <div style={displayStyle}>{expressionString}</div>
                <div>
                    {[1, 2, 3, "<"].map(num => (
                        <button key={num} 
                        style={buttonStyle} 
                        onClick={() => appendToExpression(num.toString())}>{num}</button>
                    ))}
                </div>
                <div>
                    {[4, 5, 6].map(num => (
                        <button key={num}
                        style={buttonStyle}
                        onClick={() => appendToExpression(num.toString())}>{num}</button>
                    ))}
                </div>
                <div>
                    {[7, 8, 9, 0, "( )"].map(num => (
                        <button key={num}
                        style={buttonStyle}
                        onClick={() => appendToExpression(num.toString())}>{num}</button>
                    ))}
                </div>
                <div>
                    {['+', '-', '*', '/'].map(op => (
                        <button key={op}
                        style={buttonStyle}
                        onClick={() => appendToExpression(op.toString())}>{op}</button>
                    ))}
                    <button style={equalsButtonStyle} onClick={handleEqualsSignClick}>=</button>
                </div>
            </div>
        </div>
    );
};

export default Calculator;



