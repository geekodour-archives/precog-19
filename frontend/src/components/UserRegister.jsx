import React from 'react'

const UserRegister = props => (
      <div>
      <div className="ui form">
        <div className="field">
          <label>Username</label>
          <div className="ui left icon input">
            <input placeholder="Username" type="text"/>
            <i className="user icon"></i>
          </div>
        </div>
        <div className="field">
          <label>Password</label>
          <div className="ui left icon input">
            <input type="password"/>
            <i className="lock icon"></i>
          </div>
        </div>
        <div className="ui big button"> <i className="signup icon"></i> Sign Up </div>
      </div>
      </div>
)

export default UserRegister