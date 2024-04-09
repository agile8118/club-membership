import React, { useState, useEffect, useContext } from "react";
import axios from "axios";
import Input from "../reusable/Input";
import Button from "../reusable/Button";
import alert from "../lib/alert";

const Register = () => {
  const [phoneNum, setPhoneNum] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [address, setAddress] = useState("");

  const onFormSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      await axios.post("/register", { name, email, address, phone, password });
      navigate("/login"); // after user registers, go to login page
    } catch (err) {
      if (err.response.data.error) {
        alert(err.response.data.error, "error");
      }
    }
  };

  return (
    <div className="register-container">
      <form onSubmit={onFormSubmit}>
        <label htmlFor="name">Full Name:</label>
        <div className="form-group">
          <Input
            type="name"
            id="name"
            value={name}
            onChange={(value) => setName(value)}
            placeholder=""
          />
        </div>
        <div className="form-group">
          <Input
            type="email"
            id="email"
            value={email}
            onChange={(value) => setEmail(value)}
            placeholder=""
          />
        </div>

        <div className="form-group">
          <Input
            type="address"
            id="address"
            value={address}
            onChange={(value) => setAddress(value)}
            placeholder=""
          />
        </div>

        <div className="form-group">
          <Input
            type="phone"
            id="phone"
            value={phoneNum}
            onChange={(value) => setPhoneNum(value)}
            placeholder="Phone Number"
          />
        </div>
        <div className="form-group">
          <Input
            type="password"
            id="password"
            value={password}
            onChange={(value) => setPassword(value)}
            placeholder="Password"
          />
        </div>

        <div className="form-group u-flex-text-right">
          <Button color="blue" type="submit" loading={loading}>
            Register
          </Button>
        </div>

        <div className="form-group u-text-center login-bottom-msg">
          <span>Already have an account? </span>
          <Link to="/login">Sign in.</Link>
        </div>
      </form>
    </div>
  );
};

export default Register;
