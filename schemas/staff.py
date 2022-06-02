from pydantic import BaseModel




class StaffBase (BaseModel):

    users_id: int = None

    class Config:
        orm_mode = True


class StaffCreate (StaffBase):
    pass


class StaffUpdate (StaffBase):
    pass


class Staff (StaffBase):
    id: int
