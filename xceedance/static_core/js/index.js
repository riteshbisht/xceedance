
function Feature(title, description,client, priority, target_date, product, status) {
	this.title = title;
	this.description = description;
	this.client = client;
	this.priority = priority;
	this.target_date = target_date;
	this.product = product;
	this.status = status;

}



function FeatureViewModel() {
    // Data
    var self = this;
    self.features = ko.observableArray([])
    self.availableClient = ko.observableArray([])
    self.availableProduct = ko.observableArray([
    	{'id':1,'name':'Policies'},
    	{'id':2,'name':'Billing'},
    	{'id':3,'name':'Claims'},
    	{'id':4,'name': 'Reports'}]
    )
    self.selectedProduct = ko.observable();
    self.selectedClient = ko.observable();
    self.features = ko.observableArray([]);
    self.newTitle = ko.observable();
    this.newDescription = ko.observable();
    this.newClient = ko.observable();
    this.newPriority = ko.observable();
    this.newTargetDate = ko.observable();
    this.status = ko.observable();


    self.removeFeature = function (task) {
        self.tasks.remove(task)
    };

    self.saveFeature = function () {
    	var feature = new Feature(
			this.newTitle(),
			this.newDescription(),
			this.selectedClient(),
			this.newPriority(),
			this.newTargetDate(),
			this.selectedProduct(),
			this.status()
		)
        $.ajax("/features/", {
            data: ko.toJSON(feature),
            type: "POST", contentType: "application/json",  // Always make sure to specify POST
                                                            // to avoid security holes
            success: function (result) {
            	$("#add-new-feature").modal('hide');
            	$("span[id*='error']").text("")       
                fetchInitialFeature()
            },
            error: function(error){
            	if(error['status'] == 400)
            	{
            		$("span[id*='error']").text("")       
            		error_data = error['responseJSON']
            		for (var key in error_data) {
					    // check if the property/key is defined in the object itself, not in parent
					    if (error_data.hasOwnProperty(key)) {   
					        $("#error-"+key).text(error_data[key][0])
					    }
					}
            	}
            }
        });
    };
};


featureViewModel = new FeatureViewModel()


ko.applyBindings(featureViewModel)


function fetchInitialClient(){
	 // Load initial state from server, convert it to Task instances, then populate self.tasks
    $.getJSON("/clients/", function(clientData) {
    	featureViewModel.availableClient(clientData)
    }); 

}

function fetchInitialFeature() {
	$.getJSON("/features/", function(featureData) {
    	featureViewModel.features(featureData)
    }); 
}
fetchInitialClient()
fetchInitialFeature()