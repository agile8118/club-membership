import React, { createContext, useState } from "react";
import ReactDOM from "react-dom/client";
import {
  Navigate,
  Route,
  Routes,
  BrowserRouter as Router,
} from "react-router-dom";

import Home from "./components/Home";
import Login from "./components/Login";
import Register from "./components/Register";
import Practices from "./components/Practices";
import CreatePractice from "./components/CreatePractice";
import Header from "./components/Header";

export const AppContext = createContext(null);
function App() {
  const [loggedIn, setLoggedIn] = useState(null);
  const [role, setRole] = useState(null);
  const [section, setSection] = useState("/"); // Possible values: ["/", "/login", "/register"];

  return (
    <AppContext.Provider
      value={{ loggedIn, setLoggedIn, section, setSection, role, setRole }}
    >
      <Router>
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/practice-classes" element={<Practices />} />
          <Route path="/practice-create" element={<CreatePractice />} />
        </Routes>
      </Router>
    </AppContext.Provider>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
