import React, { useState, useEffect } from 'react';
import './InfoBox.css';

function InfoBox(){
    return (
    <table>
        <tr>
            <th>Product Name:</th>
            <th>Patent Number:</th>
            <th>Country of Orgin:</th>
            <th>Status:</th>
            <th>Inventors:</th>
            <th>Company Assignee:</th>
        </tr>
    </table>
    );
}

export default InfoBox;