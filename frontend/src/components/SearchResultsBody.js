import React from 'react';
import "../styles/SearchResultsBody.css";
import SearchResultsCard from './SearchResultsCard';

const SearchResultsBody = () => {
    return (
        <div className='search-body'>
            <SearchResultsCard />
        </div>
    );
};

export default SearchResultsBody;