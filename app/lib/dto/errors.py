from pydantic import BaseModel, Field


class ApiErrorType(BaseModel):
    err_type: str
    err_code: int


class ApiErrorTypes:
    VALIDATION_ERROR = ApiErrorType(err_code=422, err_type="Validation Error")
    CALCULATOR_ERROR = ApiErrorType(err_code=422, err_type="Calculator Error")
    SERVER_ERROR = ApiErrorType(err_code=500, err_type="Server Error")


class ApiError(BaseModel):  # pydantic cannot flatten inherited models
    err_code: int = Field(..., description="HTTP Status code")
    err_type: str = Field(..., description="Type of error. User facing")
    detail: str = Field(..., description="Detailed error message - user facing")

    class Config:
        validate_assignment = True

    @classmethod
    def create_error(cls, exc, api_error_type: ApiErrorType, detail=None):
        if not detail:
            detail = str(exc)
        api_err = api_error_type.dict()

        return ApiError(**api_err, detail=detail)

    @classmethod
    def create_server_error(cls, exc, detail=None):
        return ApiError.create_error(exc, api_error_type=ApiErrorTypes.SERVER_ERROR, detail=detail)

    @classmethod
    def create_validation_error(cls, exc, detail=None):
        return ApiError.create_error(exc, api_error_type=ApiErrorTypes.VALIDATION_ERROR, detail=detail)

    @classmethod
    def create_calculator_error(cls, exc, detail=None):
        return ApiError.create_error(exc, api_error_type=ApiErrorTypes.CALCULATOR_ERROR, detail=detail)
