import React, { useEffect, useContext } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";
import { AppContext } from "../index";
import Button from "../reusable/Button";
import alert from "../lib/alert";

const Header = () => {
  const { loggedIn, setLoggedIn, section, setSection, setRole, role } =
    useContext(AppContext);

  const navigate = useNavigate();

  const checkLoggedIn = async () => {
    try {
      const { data } = await axios.post(
        "/is-logged-in",
        {},
        { headers: { Authorization: localStorage.getItem("token") } }
      );

      setLoggedIn(true);
      setRole(data.role);
    } catch (err) {
      setRole(null);
      setLoggedIn(false);
    }
  };

  useEffect(() => {
    checkLoggedIn();
  }, [loggedIn]);

  useEffect(() => {
    setSection(window.location.pathname);
  }, [section]);

  const logout = async () => {
    try {
      /** @API call */
      await axios.delete("/logout", {
        headers: { Authorization: localStorage.getItem("token") },
      });
      localStorage.removeItem("token");
      setLoggedIn(false);
      setSection("/");
      alert("Logged out successfully!", "success");
    } catch (e) {
      alert("Sorry an unexpected error happened.", "error");
    }
  };

  return (
    <div className="header">
      <div className="header__left">
        <Link
          className="header__link header__link--home"
          to="/"
          onClick={() => {
            setSection("/");
          }}
        >
          Home
        </Link>
      </div>
      <div className="header__right">
        {section !== "/login" && !loggedIn && (
          <Link
            className="header__link header__link--login"
            to="/login"
            onClick={() => {
              setSection("/login");
            }}
          >
            Login
          </Link>
        )}

        {section !== "/practice-classes" && role === "member" && loggedIn && (
          <Link
            to="/practice-classes"
            className="header__link header__link--profile"
            onClick={() => {
              setSection("/practice-classes");
            }}
          >
            Classes
          </Link>
        )}

        {section !== "/practice-create" && role === "treasurer" && loggedIn && (
          <Link
            to="/practice-create"
            className="header__link header__link--profile"
            onClick={() => {
              setSection("/practice-create");
            }}
          >
            Create Class
          </Link>
        )}

        {section !== "/profile" && loggedIn && (
          <Link
            to="/profile"
            className="header__link header__link--profile"
            onClick={() => {
              setSection("/profile");
            }}
          >
            Profile
          </Link>
        )}

        {loggedIn && (
          <Link
            className="header__link header__link--logout"
            to="/"
            onClick={() => {
              logout();
            }}
          >
            Logout
          </Link>
        )}
      </div>
    </div>
  );
};

export default Header;
