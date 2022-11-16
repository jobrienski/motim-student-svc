-- This init script is ONLY executed ONCE by postgres!
-- If you make changes to this script and need it reran,
-- you will have to delete the db-data folder then
-- rebuild and rerun the db docker image

-- This init script is ONLY for your local environment and CI!
-- Our real environments (dev, staging, prod, etc) do NOT use this!
-- Instead, we use Terraform to stand up RDS

CREATE DATABASE studentsdb;
