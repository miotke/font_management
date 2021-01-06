//
//  SystemButton.swift
//  Fonts
//
//  Created by Miotke, Andrew on 1/5/21.
//

import UIKit

class SystemButton: UIButton {
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        styleButton()
    }
    
    func styleButton() {
        self.frame = CGRect(x: 100, y: 10, width: 100, height: 35)
        self.backgroundColor = UIColor.systemOrange
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
