-- 3 first students IN the Batch ID=3 
-- because Batch 3 is the best!
SELECT column_name, data_type, character_maximum_length, is_nullable 
FROM information_schema.columns 
WHERE table_name = 'first_table' 
  AND table_schema = 'hbtn_0c_0';