

-- def __init__(self, id, title, desc, time, up, down, approved, industry, resolved):
--         self._Review_ID = id
--         self._Title = title
--         self._Description = desc
--         self._Read_Time = time
--         self._Upvote = up
--         self._Downvote = down
--         self._Approved = approved
--         self._Industry = industry
--         self._Resolved = resolved


CREATE TABLE Posts (
    Review_ID INT NOT NULL,
    Product_ID TEXT NOT NULL,
    Title TEXT NOT NULL,
    Description TEXT NOT NULL,
    Read_Time INT NOT NULL,
    Num_Upvotes INT NOT NULL,
    Num_Downvotes INT NOT NULL,
    Approved TEXT NOT NULL,
    Industry TEXT NOT NULL,
    Is_Resolved TEXT NOT NULL,
    Solution TEXT );

CREATE TABLE Comments (
    Comment_ID INT NOT NULL,
    Review_ID INT NOT NULL,
    Body TEXT NOT NULL,
    U_ID TEXT NOT NULL,
    Num_Upvotes INT,
    Num_Downvotes INT
);

CREATE TABLE Products(
    Product_ID TEXT NOT NULL,
    Name TEXT NOT NULL,
    Link TEXT
);

INSERT INTO Posts (Review_ID, Product_ID, Title, Description, Read_Time, Num_Upvotes, Num_Downvotes, Approved, Industry, Is_Resolved, Solution)
    VALUES(1, '4UJ42', 'Recommendation For Lubricant For Heavy Load Machinery? ', 'Customer is looking for a bearing grease suitable for heavly-load machinery being assembled on conveyors in manufacturing enviorments.',
    10, 10, 2, 'Y', 'Manufacturing', 'Y', 
    'A High-Temperature extreme bearing grease is commonly used in manufacturing enviorments, it can also take on heavier loads. Manufacturing assembly lines often have high-speeds and extreme-pressure which this lubricant can handle. LPS Multi-Purpos for a Mineral oil base. KRYTOX XHT for a synthetic oil base. '),
    (2, '4UJ34', 'Lubricant for Construction?', 'Customer is a manager on a construction team looking for a lubricant that can work on multiple tools and machines.',
    10, 7, 3, 'Y', 'Construction', 'Y', '3-In-One is a reliable well known general lubricant that comes in a squeeze bottle. Leaves slippery coating to extend life of equpment and provide some protection against water damage, contaminants, and corrosives.'),
    (3, '4PKE9', 'Looking for product that can help with optimizing equipment performance?', 'Customer is looking for something that can help with optimizing equopment perfomance within the manfucatruing factory and increase efficiency.',
    10, 10, 2, 'Y', 'Manufacturing', 'Y', 'An electrical properties data logger would work well. Electrical properties data loggers detect, measure, and record various electrical properties such as current, voltage, frequency, and phase. They are commonly used for maintenance and repair to verify system parameters, improve system efficiency, and help reduce downtime.'),
    (4, 'KH78L', 'Product for manufacturing', 'Something that will help with optimizinf equpment performance.', 8, 0, 5, 'N', 'Manufacturing',
    'Y', ' '),
    (6, 'N/A', 'General suggestions for improving efficiency in manufacturing?',
     'Looking for general ways and products to improve overall efficiency within manufacturing and factories.', 8, 15, 0, 'N', 'Manufacturing',
    'N', '1.) Material Handling Equpment, Material handling equipment is used to move, store, or ship items efficiently. Conveyor systems reduce the effort it takes to move heavy or bulky materials from one location to another. 2.) Test Intruments,Test instruments and diagnostic test equipment help users isolate and solve problems and maintain vital processes, before they interrupt their work or cause hazards in the facility.');

INSERT INTO Products(Product_ID, Name, Link){
    VALUES('4UJ42', 'LPS Multipurpose Bearing Grease', 'https://www.grainger.com/product/LPS-Multipurpose-Bearing-Grease-4UJ42'),
    ('4UJ34', '3-IN-ONE Machine Oil: Multipurpose Oil', 'https://www.grainger.com/product/3-IN-ONE-Machine-Oil-Multipurpose-Oil-4UJ34'),
    ('4PKE9','AEMC Voltage Data Logger','https://www.grainger.com/product/AEMC-Voltage-Data-Logger-0-5-AC-4PKE9?searchQuery=4PKE9&searchBar=true&tier=Not+Applicable')

}