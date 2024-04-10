import React, { useState, useEffect, useContext } from "react";
import axios from "axios";
import { AppContext } from "../index";
import { useNavigate, Link } from "react-router-dom";
import Input from "../reusable/Input";
import Button from "../reusable/Button";
import alert from "../lib/alert";

const Practices = () => {
  const navigate = useNavigate();

  return (
    <div className="login-container">
      <h1>
        Here I as a member should see all the upcoming practice sessions and be
        able to sign up for each on!
      </h1>
    </div>
  );
};

export default Practices;
