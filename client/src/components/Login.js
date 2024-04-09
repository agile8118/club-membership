import React, { useState, useEffect, useContext } from "react";
import { useNavigate, Link } from "react-router-dom";
import axios from "axios";
import { AppContext } from "../index";
import Input from "../reusable/Input";
import Button from "../reusable/Button";
import alert from "../lib/alert";

const Login = () => {
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const { loggedIn, setLoggedIn, setSection } = useContext(AppContext);

  const navigate = useNavigate();

  const onFormSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      /** @API call */
      const { data } = await axios.post("/login", { phone, password });
      localStorage.setItem("token", data.token);
      alert("Logged in successfully!", "success");

      setLoggedIn(true);
      navigate("/");
      setSection("/");
    } catch (err) {
      if (err.response.data.error) {
        alert(err.response.data.error, "error");
      }
    }
    setLoading(false);
  };

  return (
    <div className="login-container">
      <h2 className="u-text-center">Login</h2>
      <form onSubmit={onFormSubmit}>
        <div className="form-group">
          <Input
            type="phone"
            label="Phone Number"
            value={phone}
            onChange={(value) => {
              setPhone(value);
            }}
          />
        </div>
        <div className="form-group">
          <Input
            type="password"
            label="Password"
            value={password}
            onChange={(value) => {
              setPassword(value);
            }}
          />
        </div>

        <div className="form-group u-flex-text-right">
          <Button color="blue" type="submit" loading={loading}>
            Login
          </Button>
        </div>

        <div className="form-group u-text-center login-bottom-msg">
          <span>Don't have an account? </span>
          <Link to="/register">Create one.</Link>
        </div>
      </form>
    </div>
  );
};

export default Login;
