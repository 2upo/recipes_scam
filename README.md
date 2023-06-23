This project is telegram bot for scanning recipes.

TODO:

- [ ] database
- [ ] service
- [ ] tg_client
- [ ] main
- [ ] docker + postgres (data is persisted on volume)
- [ ] migrations
- [ ] refactor and beautify
- [ ] translate
- [ ] categorize




```
#    USE CASES
# +-------------------------------------------------------------------------------------------------------------------------------+
# |        tg chat id                        data                    start proc                                                   |
# |  User ----------->   1. Send photoes. -----------> Telegram bot ------------>  OCR                                            |
# |    |                                                                           |                                              |
# |    |  <------------------------------------------- Text convertor<-------------+                                              |
# |    |                Send to User                                    rec. text                                                 |
# |    |                                                 |                                                                        |
# |    |                                                 |                                                                        |
# |    |                                                 +----------------- Extract: price & name + Overall amount                |
# |    |                                                                                                                          |
# |    |                                                                                                                          |
# |    |                                                                                                                          |
# |    +--------------->  2. Appove    -----------------------------  Save to db result                                           |
# |    |                                                                                                                          |
# |    |                                                                                                                          |
# |    +--------------->  3. Discard   ------------------------------>  Clear temp record in db                                   |
# |    |                                                                                                                          |
# |    |                                                                                                                          |
# |    |                                                                                                                          |
# |    +---------------------------> register + for security reasons promt user to enter secret number                            |
# |    |                                                                                                                          |
# |    +-------------->  4. Statistics ------------------------  Render statistics png's for certain period with pandas dataframe |
# |                                                                                                                               |
# +-------------------------------------------------------------------------------------------------------------------------------+
#  DATA MODEL
# +-------------------------------------------------------------------------------------------------------------------------------+
# |                                                                                                                               |
# | User                  Purchase               CartItems                                                                        |
# | ---------------       ----------------       ----------------                                                                 |
# | id: int        <-----+id: int          <----+id                                                                               |
# | chat_id: str         |overall: !!! int      |name                                                                             |
# | is_active: bool      |created_at: dt        |name_translated                                                                  |
# |                      |is_commited: bool     |purchase_id                                                                      |
# |                      |user_id: int           price                                                                            |
# |                                                                                                                               |
# | 1. If "Discard" --> ALL Purchases where is_commited = False need to be removed.                                               |
# |                                                                                                                               |
# | 2. Before every action, check if user is_active = True.                                                                       |
# |                                                                                                                               |
# | 3. User receives photo of recognized table + json text of Purchase and related CartItems. User can send                       |
# |    this JSON to edit specific values. Better to use not JSON, but CSV. <-------- !!! Important !!!                            |
# |                                                                                                                               |
# |                                                                                                                               |
# |                                                                                                                               |
# |                                                                                                                               |
# |                                                                                                                               |
# |                                                                                                                               |
# +-------------------------------------------------------------------------------------------------------------------------------+
```
