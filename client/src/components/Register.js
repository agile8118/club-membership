import React, { useState, useEffect, useContext } from "react";


const Register = () => {
    const [phoneNum, setPhoneNum] = useState("");
    const [password, setPassword] = useState("");
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [address, setAddress] = useState("");

    const handleLogin = () => {

        console.log("User logged in with phone", phoneNum);

    }

    
    return (
        <div>
            <label htmlFor="name">Full Name:</label>
            <input 
                type="name"
                id="name"
                value={ name }
                onChange={(e) => setName(e.target.value)}
                placeholder=""
            />

            <label></label>
            <input 
                type="email"
                id="email"
                value={ email }
                onChange={(e) => setEmail(e.target.value)}
                placeholder=""
            />

            <label></label>
            <input 
                type="address"
                id="address"
                value={ address }
                onChange={(e) => setAddress(e.target.value)}
                placeholder=""
            />

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

export default Register;
