import React, { Component } from 'react';
import { Row, Col, Card, CardBody, Button, UncontrolledDropdown, UncontrolledTooltip, Dropdown, DropdownToggle, DropdownMenu, DropdownItem, Form, FormGroup, Input, InputGroup, InputGroupAddon } from "reactstrap";
import { Link } from "react-router-dom";
import 'font-awesome/css/font-awesome.min.css';
import CollapsAnother from "./Tabes"


//Simple bar
import SimpleBar from "simplebar-react";

const tableborder = {
    td:{
            border:"1px solid black" }
        }

class ProfitAndLoss extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <React.Fragment>
                        <center>


            <h2 style={{marginTop:"10%"}}></h2></center>
                            <Col style={{marginTop:"2%",marginLeft:"5%",marginBottom:"10%"}} xl="11">
                                <Card>
                                    <table className="table">
                                      <thead className="thead-dark">
                                        <tr>
                                          <th style={{width:"30%"}} scope="col"><center>Profit And Loss</center></th>
                                        </tr>
                                      </thead>
                                     </table>

                                        <CollapsAnother/>


                                </Card>
                            </Col>
            </React.Fragment>
        );
    }
}

export default ProfitAndLoss;