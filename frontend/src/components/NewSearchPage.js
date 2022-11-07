import React, { useState } from 'react';
import { variables } from '../Variables';

const NewSearchPage = () => {
    const [data, setData] = useState([]);

    fetch(variables.API_URL+'car')

    return (
        <div>
            {data.map(item =>
                <div key={item.id}>
                </div>)}
        </div>
    );
};

export default NewSearchPage;