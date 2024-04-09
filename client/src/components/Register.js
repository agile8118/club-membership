import React, { useState, useEffect, useContext } from "react";
import axios from "axios";
import { AppContext } from "../index";
import { useNavigate, Link } from "react-router-dom";
import Input from "../reusable/Input";
import Button from "../reusable/Button";
import alert from "../lib/alert";

const Register = () => {
  const [phoneNum, setPhoneNum] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [address, setAddress] = useState("");
  const [loading, setLoading] = useState(false);
  const { loggedIn, setLoggedIn, setSection } = useContext(AppContext);

  const navigate = useNavigate();

  const onFormSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const { data } = await axios.post("/register", {
        name,
        email,
        address,
        phone: phoneNum,
        password,
      });
      alert("Registered successfully!", "success");
      localStorage.setItem("token", data.token);

      setLoggedIn(true);
      navigate("/");
      setSection("/");
    } catch (err) {
      console.log(err);
      if (err.response.data.error) {
        alert(err.response.data.error, "error");
      }
    }

    setLoading(false);
  };

  return (
    <div className="login-container">
      <h2 className="u-text-center">Register</h2>
      <form onSubmit={onFormSubmit}>
        <div className="form-group">
          <Input
            type="name"
            required
            label="Name"
            value={name}
            onChange={(value) => setName(value)}
          />
        </div>
        <div className="form-group">
          <Input
            type="email"
            label="Email"
            required
            value={email}
            onChange={(value) => setEmail(value)}
          />
        </div>

        <div className="form-group">
          <Input
            type="address"
            label="Address"
            required
            value={address}
            onChange={(value) => setAddress(value)}
          />
        </div>

        <div className="form-group">
          <Input
            type="phone"
            value={phoneNum}
            required
            onChange={(value) => setPhoneNum(value)}
            label="Phone Number"
          />
        </div>
        <div className="form-group">
          <Input
            type="password"
            required
            value={password}
            onChange={(value) => setPassword(value)}
            label="Password"
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
