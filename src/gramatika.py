program             :           declarations

declarations        :           (include_library | function_declaration | var_declaration_list)*

include_library     :           REGAR ID SEMICOLON

variable            :           ID

type_spec           :           TYPE

function_decleration:           TOR ID COLON COLON LPAREN parameters RPAREN function_body

function_body       :           LBRACKET statement_list RBRACKET

parameters          :           empty
                                | param (COMMA param)*

param               :           variable COLON type_spec

function_call       :           ID COLON (expr | STRING)?

factor              :           PLUS factor
                                | MINUS factor
                                | AMPERSAND variable
                                | INT_NUMBER
                                | LPAREN expr RPAREN
                                | variable
                                | function_call

expr                :           term ((PLUS | MINUS | LSQUARE_BRACKET RSQUARE_BRACKET | GRATER | LESS | GRATER_EQUAL | LESS_EQUAL) term)*

term                :           factor ((MUL | DIV) factor)*

var_declaration_list:           LOK var var_initialization (COMMA var var_initialization)* SEMICOLON

var_initialization  :           (ASSIGN expr)?

assignment_statement:           variable ASSIGN expr SEMICOLON

return_statement    :           ZET expr SEMICOLON

if_statement        :           ZUG expr QUESTION_MARK stm_body (RUH stm_body)

while_statement     :           SWOBU expr QUESTION_MARK stm_body

for_statement       :           GOR ID ASSIGN factor GAR factor stm_body

foreach_statement   :           GOR ID GON ID stm_body

list_indexing       :           ID AT_SIGN INT

stm_body            :           LBRACKET statement_list RBRACKET

True                :           DAR

False               :           NAR

and                 :           KUG

or                  :           TUK




statement_list              : var_declaration_list
							| statement
							| statement statement_list

statement                   : assignment_statement
							| function_call SEMICOLON
							| if_statement
							| return_statement
							| empty