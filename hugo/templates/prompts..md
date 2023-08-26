SELECT * FROM mindsdb.models.my_model JOIN mindsdb.input_data_name;   

-- CREATE MODEL open_ai.stock_photos
-- PREDICT img_url
-- USING
--    engine = 'openai',
--    mode = 'image',
--    prompt_template = '{{text}}, 8K | highly detailed 1920 x 1080px photographs in the style of stock photography found on Unsplash, Pexels, Shutterstock, and Adobe Stock';



SELECT * 
FROM open_ai.stock_photos
WHERE text = 'A stock photograph of a small white notebook on an empty white desk with a vibrant, bright orange stock background and lots of room for copy space. Modern, clean look. 1024px x 1024px;'


SELECT * 
FROM open_ai.stock_photos
WHERE text = '3d render simple minimal toy art kaws styles of a cute cartoon fat shih tzu barking, modern minimalist;'

