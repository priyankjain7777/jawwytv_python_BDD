Feature: Validate the Subscription Packages Type
 Scenario: verify the package
   Given open chrome browser
   When open jawwaytv homepage
   Then change language to english

   Then check the lite pack
   Then check the lite pack price

   Then check the classic pack
   Then check the classic pack price

   Then check the premium pack
   Then check the premium pack price


   And  close browser

