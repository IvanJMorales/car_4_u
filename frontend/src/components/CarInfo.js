import React from 'react';
import '../styles/CarInfo.css';

import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';
import { Link } from 'react-router-dom';

const CarInfo = () => {
    const data = []
    return (
        <div className='carInfo-container'>
            {data.data.slice(0,1).map((option) => (
                <Card className='carInfo' key={option.index} value={option.carmake}>
                        <CardActionArea>
                                <CardMedia
                                    component="img"
                                    alt="CAR IMAGE"
                                    height="500"
                                    image={option.image}
                                />
                        </CardActionArea>
                        <CardContent className='card-content'>
                            <Typography className='card-title' variant="h4">
                                {option.name}
                            </Typography>
                            <Typography className='carInfo-card-info' variant="h5" color="text.secondary">
                                Price: ${option.price}
                                <br></br>
                                Milage: {option.miles}
                                <br></br>
                                Year: {option.year}
                                <br></br>
                                Milage: {option.miles}
                                <br></br>
                                Engine: {option.engine}
                            </Typography>
                        </CardContent>
                        <CardActions className='actions'>
                            <a href={option.link}>
                                <Button size="small">Go to site</Button>
                            </a>
                        </CardActions>
                </Card>
            ))}
        </div>
    );
};

export default CarInfo;