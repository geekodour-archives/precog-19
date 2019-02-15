import React from 'react'

const UserLogin = props => (
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
      <div className="ui blue submit button">Login</div>
    </div>
)

export default UserLogin