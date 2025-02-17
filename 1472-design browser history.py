#this exercise asks to build webhistory (doubly linked lists)
#problem: https://leetcode.com/problems/design-browser-history/description/
class ListNode:
    #node for the linked list (browser history)
    #next and prev act as the browser history allowing you to go forward or back in your history
    #prev points to previous website
    #next points to next website
    def __init__(self, url: str):
        self.url = url
        self.next = None 
        self.prev = None

class BrowserHistory:
    #initialize the list with a given url as the homepage
    def __init__(self, homepage: str):
        self.curr= ListNode(homepage) #curr represents the current webpage the browser is on
    
        
    #from the current url visit a newsite
    #links the current site and new site together via prev and next pointers
    #this is different than using the back or forward functions as it will rewrite the browser history
    #the next pointer of the current webpage will be rewritten to be the given webpage
    def visit(self, url: str) -> None:
        NewSite = ListNode(url)
        NewSite.prev = self.curr
        self.curr.next = NewSite
        self.curr = self.curr.next

    #goes back in history by a given amount of steps
    #only goes back as far as it can
    def back(self, steps: int) -> str:
        while(steps and self.curr.prev):
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

    #goes forward in history by a given amount of steps
    #only goes forward as far as it can
    def forward(self, steps: int) -> str:
        while(steps and self.curr.next):
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url
