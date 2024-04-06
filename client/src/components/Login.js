import React, { useState, useEffect, useContext } from "react";


const Login = () => {
    const [phoneNum, setPhoneNum] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = () => {

        console.log("User logged in with phone", phoneNum);

    }

    
    return (
        <div>
            <label htmlFor="phone">Phone Number:</label>
            <input 
                type="phone"
                id="phone"
                value={ phoneNum }
                onChange={(e) => setPhoneNum(e.target.value)}
                placeholder="Phone Number"
            />

            <label htmlFor="password">Password:</label>
            <input 
                type="password"
                id="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
            />

            <button onClick={handleLogin}>Log In</button>

        </div>
    );
};

export default Login;
