import React, { useState, useEffect, useContext } from "react";
import axios from "axios";
import { AppContext } from "../index";
import { useNavigate, Link } from "react-router-dom";
import Input from "../reusable/Input";
import Button from "../reusable/Button";
import alert from "../lib/alert";

const CreatePractice = () => {
  const navigate = useNavigate();

  return (
    <div className="login-container">
      <h1>
        Here I as a treasurer should be able to see a form and create a new
        practice session!
      </h1>
    </div>
  );
};

export default CreatePractice;
